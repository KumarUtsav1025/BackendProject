from django.urls import path,include
from Project.views import PostAPI, post_comment, react
from rest_framework import routers


urlpatterns = [
    path('', PostAPI.as_view()),
    path('<int:pk>/post_comment/',post_comment, name= "comment_api"),
    path('<int:pk>/<arg>/<num>/', react, name= "react_api"),
]