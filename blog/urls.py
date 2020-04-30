from django.urls import path
from . import views
from .views import (
   PostListView,
   PostDetailView,
   PostCreateView,
   PostUpdateView,
   PostDeleteView,
   UserPostListView
)

urlpatterns = [
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_create'),
    path('home/',PostListView.as_view(), name='blog-home'),
   path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
   path('post/new/',PostCreateView.as_view(), name='post-create'),
   path('about/', views.about , name='blog-about'),
]