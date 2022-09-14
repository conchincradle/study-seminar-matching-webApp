from django.shortcuts import render, redirect
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
