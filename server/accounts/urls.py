from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('users/<int:pk>/', views.MypageView.as_view(), name='my_page'),
    path('users/<int:pk>/', views.MypageView.as_view(), name='my_page'),
]