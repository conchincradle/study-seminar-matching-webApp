from django.urls import path
from accounts import views

urlpatterns = [
    path('follow_user/', views.SignupView.as_view(), name='follow_user'),
]