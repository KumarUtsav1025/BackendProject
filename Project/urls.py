from django.urls import path
from Project.views import PostAPI

urlpatterns = [
    path('', PostAPI.as_view())
]