from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home/', views.IndexView.as_view(), name='index'),
    path('study/', views.IndexStudyView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('study/<int:pk>', views.PostStudyDetailView.as_view(), name='post_study_detail'),
    path('study/<int:pk>/participate', views.PostStudyLinkView.as_view(), name='study_participate'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('study/new/', views.CreatePostStudyView.as_view(), name='post_sutdy_new'),
    path('post/study/<int:pk>', views.PostStudyDetailView.as_view(), name='post_study_detail'),
    path('post/<int:pk>/edit', views.PostEditView.as_view(), name='post_edit'),
    path('study/<int:pk>/edit', views.PostStudyEditView.as_view(), name='post_study_edit'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
    path('study/<int:pk>/delete', views.PostStudyDeleteView.as_view(), name='post_study_delete'),
    


]