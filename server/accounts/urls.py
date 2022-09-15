from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('mypage/<int:pk>/',views.MypageView.as_view(), name='account_mypage'),
    path('mypage/edit', views.ProfileUpdateView.as_view(), name='edit_page'),
    path('userpage/<int:pk>',views.userpage, name='account_userpage'),
    path('profile/<int:pk>',views.ProfileView.as_view(), name='account_profile'),
    path('plan/<int:pk>/',views.PlanView.as_view(), name='account_plan'),

]
