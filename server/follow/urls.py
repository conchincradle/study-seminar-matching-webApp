from django.urls import path
# from follow import views
from . import views

# テスト用
urlpatterns = [
    path('following/',views.following, name='following'),
    path('followers/',views.followers, name='followers'),
]