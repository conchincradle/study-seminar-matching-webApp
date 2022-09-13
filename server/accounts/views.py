from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account import views

class LoginView(views.LoginView):
    template_name = 'accounts/login.html'

class LogoutView(views.LogoutView):
    template_name = 'accounts/logout.html'

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.logout()
        return redirect('/')

class SignupView(views.SignupView):
    template_name = 'accounts/signup.html'

#LoginRequiredMixin ログイン必須
class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/my_page.html' #仮

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staff_list'] = Staff.objects.filter(user=self.request.user).order_by('name')
        context['schedule_list'] = Schedule.objects.filter(staff__user=self.request.user, start__gte=timezone.now()).order_by('name')
        return context