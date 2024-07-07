from django.urls import path
from .views import BlogListCreateAPI, BlogDetailAPI

urlpatterns = [
    path('', BlogListCreateAPI.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetailAPI.as_view(), name='blog-detail'),
]
