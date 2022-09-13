from django.urls import path
# from follow import views
from . import views

# テスト用
urlpatterns = [
    path('follow_user/',views.follow_user, name='follow'),
]