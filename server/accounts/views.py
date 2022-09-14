from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileEditForm
from .models import AccountUser
from django.views import generic
from allauth.account import views
from django.utils import timezone
from .forms import UserForm
from django.views.generic import View


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

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = AccountUser
#     form_class = ProfileEditForm
#     template_name = 'accounts/post_form.html'
class ProfileUpdateView(LoginRequiredMixin, FormView):
    template_name = 'accounts/post_form.html'
    form_class = ProfileEditForm
    # success_url = reverse_lazy('accounts:profile')
    
    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'user_name' : self.request.user.user_name,
            'profile' : self.request.user.profile,
            'birthday' : self.request.user.birthday,
        })
        return kwargs
#LoginRequiredMixin ログイン必須
class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/my_page.html' #仮

    def get(self, request, *args, **kwargs):
        post_data = AccountUser.objects.get(id=self.kwargs['pk'])
        form = ProfileEditForm(
            request.POST or None,
            initial = {
                'name': post_data.name,
                'profile': post_data.profile,
                'birthday':post_data.birthday
            }
        )

        return render(request, 'accounts/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST or None)

        if form.is_valid():
            post_data = AccountUser.objects.get(id=self.kwargs['pk'])
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', post_data.id)
        
        return render(request, 'accounts/post_form.html', {
            'form':form
        })      
# mypage test-Zhu
def mypage(request):
    context = {
            'user_icon':"https://iconutopia.com/wp-content/uploads/2016/06/space-dog-laika1.png",
            'user_name': 'ラブパイ',
            "profile":'''私はプログラミングに関するスキルの幅広さに自信があります。C言語やPHPはもちろん、Rubyに関しても知見がありますので、
                      幅広い業務に対応できる強みがあります。また、現在はScalaを独学で学んでおり、
                      今後も状況に応じて必要性の高いプログラミング言語を中心に学んでいきたいと考えております。''',
            "sound_profile":"",
            "birthday":timezone.now(),

            }
    return render(request,'accounts/mypage.html',context)

def userpage(request):
    context = {
            'user_icon':"https://iconutopia.com/wp-content/uploads/2016/06/space-dog-laika1.png",
            'user_name': 'ラブパイ',
            "profile":'''私はプログラミングに関するスキルの幅広さに自信があります。C言語やPHPはもちろん、Rubyに関しても知見がありますので、
                      幅広い業務に対応できる強みがあります。また、現在はScalaを独学で学んでおり、
                      今後も状況に応じて必要性の高いプログラミング言語を中心に学んでいきたいと考えております。''',
            "sound_profile":"",
            "birthday":timezone.now(),

            }
    return render(request,'accounts/userpage.html',context)

'''
from django.core.files.base import ContentFile
def save_file(request):
    mymodel = MyModel.objects.get(id=1)
  
    file_content = ContentFile(request.FILES['video'].read())
 
    mymodel.video.save(request.FILES['video'].name, file_content)
'''

###### test zhu

def profile(request):
    return render(request,"accounts/profile.html")

class ProfileView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        # <view logic>
        return render(request, 'accounts/profile.html',form)
    def post(self,request, *args, **kwargs):
        form = UserForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            context = {}
            context.user_icon = form.cleaned_data['user_icon']
            context.birthday = form.cleaned_data['birthday']
            context.profile = form.cleaned_data['profile']
            context.sound_profile = form.cleaned_data['sound_profile']
            print(context)

            # redirect to a new URL:
            return render(request, 'accounts/mypage.html', context)
        else:
            print("nonvalid")
            return render(request, 'accounts/profile.html')
