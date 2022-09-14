from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.IndexView.as_view(), name='index'),
    path('home/study/', views.IndexStudyView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/study/<int:pk>', views.PostStudyDetailView.as_view(), name='post_study_detail'),
    path('post/study/<int:pk>/participate', views.PostStudyLinkView.as_view(), name='study_participate'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/study/new/', views.CreatePostStudyView.as_view(), name='post_sutdy_new'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    


]