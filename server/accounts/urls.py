from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('users/', views.MypageView.as_view(), name='edit_page'),
    path('mypage/',views.mypage, name='account_mypage'),
    path('userpage/',views.userpage, name='account_userpage'),
]