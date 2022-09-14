from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileEditForm
from .models import Post
from allauth.account import views
from django.utils import timezone

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

    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = ProfileEditForm(
            request.POST or None,
            initial = {
                'name': post_data.name,
                'profile': post_data.profile,
                'birthday':post_data.birthday
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', post_data.id)
        
        return render(request, 'app/post_form.html', {
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

from django.core.files.base import ContentFile


# test

def save_file(request):
    mymodel = MyModel.objects.get(id=1)
    # 读取上传的文件中的video项为二进制文件
    file_content = ContentFile(request.FILES['video'].read())
    # ImageField的save方法，第一个参数是保存的文件名，第二个参数是ContentFile对象，里面的内容是要上传的图片、视频的二进制内容
    mymodel.video.save(request.FILES['video'].name, file_content)
###### test zhu
