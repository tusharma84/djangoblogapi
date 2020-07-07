from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.PostListView.as_view()),
    path('comment/', views.CommentListView.as_view()),
    path('create/post/', views.PostCreateView.as_view()),
    path('create/comment/', views.PostCreateView.as_view()),
    path('getpost/<int:pk>/', views.PostDetailView.as_view()),
]
