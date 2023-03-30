from django.urls import path
from Project.views import PostAPI, CommentAPI

urlpatterns = [
    path('', PostAPI.as_view()),
    path('<int:pk>/post_comment/',CommentAPI.as_view())
]