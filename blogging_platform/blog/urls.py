from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:id>/delete/', views.post_delete, name='post_delete'),
    path('signup/', views.signup, name='signup'),
    path('post/<int:post_id>/ai-summary/', views.ai_summary, name='ai_summary'),
    path('post/<int:post_id>/ai-comment-suggestion/', views.ai_comment_suggestion, name='ai_comment_suggestion'),
    path('ai-writer/', views.ai_blog_writer, name='ai_blog_writer'),
    path('ai-generate/', views.ai_generate_post, name='ai_generate_post'),
]