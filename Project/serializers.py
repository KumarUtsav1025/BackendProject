from rest_framework import serializers
from Project.models import Post, Comment, PostImage

class PostImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "image"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "commentText"]
        
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        depth = 1
        model = Post
        fields = "__all__"

    post_comment  = serializers.SerializerMethodField()
    images =  PostImageSerializers(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    def get_post_comment(self, obj):
        Post_obj = Comment.objects.filter(post_id = obj.id)
        serializer = CommentSerializer(Post_obj, many = True)
        return serializer.data
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        post = Post.objects.create(**validated_data)

        for image in uploaded_images:
            PostImage.objects.create(post = post, image=image)

        return post
    
