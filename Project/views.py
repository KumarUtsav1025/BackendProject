from rest_framework.decorators import APIView, api_view
from Project.serializers import PostSerializer, CommentSerializer
from Project.models import Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.paginator import Paginator

# Create your views here.

class PostAPI(APIView):
    
    parser_class = [MultiPartParser, FormParser]

    def get(self, request):
        objs = Post.objects.all()
        try:
            page = request.GET.get('page',1)
            page_size = 10
            paginator  = Paginator(objs, page_size)
            serializer = PostSerializer(paginator.page(page), many = True)
        except Exception as e:
            return Response({
                'status' : 'False',
                'message': 'Empty Page'
                }, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PostSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    
    # def put(self, request):
    #     data = request.data
    #     obj=Post.objects.get(id = data['id'])
    #     serializer = PostSerializer(obj, data= data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    
    # def patch(self, request):
    #     data = request.data
    #     obj=Post.objects.get(id = data['id'])
    #     serializer = PostSerializer(obj, data= data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    
    # def delete(self, request):
    #     data = request.data
    #     obj=Post.objects.get(id = data['id'])
    #     obj.delete()
    #     return Response({'message':'Post deleted'})
    

@api_view(['POST'])
def post_comment(request, pk):
        data = request.data
        data= {"post": pk, "commentText" : data['commentText']}
        serializer = CommentSerializer(data=data)
        print("hello")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['PUT'])
def react(request, pk, arg, num):
    obj=Post.objects.get(id = pk)
    data= {arg : num}
    serializer = PostSerializer(obj, data= data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    