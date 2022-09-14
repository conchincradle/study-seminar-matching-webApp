from django.urls import path

from follow import views


# テスト用
urlpatterns = [
    path('followings/<int:user_id>', views.followings.as_view(), name='followings'),
    path('followers/<int:user_id>', views.followers.as_view(), name='followers'),
]

