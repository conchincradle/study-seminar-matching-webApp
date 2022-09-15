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
from app.models import AppSeminar


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


class MypageView(LoginRequiredMixin, View):
    template_name = 'accounts/mypage.html' #仮

    def calculate_age(self,born):
        today = timezone.now()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        sedai = age- age%10
        return sedai

    def get(self, request, *args, **kwargs):
        user = request.user

        print(type(AccountUser.user_name))
        print(AccountUser.objects.values())
        print("-------------------------------")
        print(AccountUser.objects.values())
        post_data = AccountUser.objects.get(user_name=user.pk)
        print(post_data)
        sedai = self.calculate_age(post_data.birthday)
        context={
            'user_name': user.username,
            'user_icon': post_data.user_icon,
            'profile': post_data.profile,
            'sound_profile': post_data.sound_profile,
            'sedai': sedai,


        }
        print(post_data.user_icon)

        return render(request, 'accounts/mypage.html', context)

    
    
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
class PlanView(LoginRequiredMixin, View):
    def get(self,request,*args,**kwargs):

        print("------------------")
        #postData = AppSeminar.objects.filter(author_id=user.pk)
        content = {
            'title': 'ABC study group seminar',
            'content': "We will hold the ,meeting between 13:00-15:00 on 9/17. ",
            'zoom_link': "zoom_link",
        }


        return render(request, 'accounts/plan.html',{'content': content})



def userpage(request):
    print(target_user.id)
    post_data = AccountUser.objects.get(user_name=user.pk)
    print(post_data)
    sedai = self.calculate_age(post_data.birthday)
    context = {
        'user_name': user.username,
        'user_icon': post_data.user_icon,
        'profile': post_data.profile,
        'sound_profile': post_data.sound_profile,
        'sedai': sedai,

    }
    print(post_data.user_icon)


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
        form = UserForm(request.POST or None)
        # <view logic>
        return render(request, 'accounts/profile.html',{"form":form})
    def post(self,request, *args, **kwargs):
        print(request.POST)
        form = UserForm(request.POST or None)
        # check whether it's valid:
        print(form)

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            #print(AccountUser.objects.get(id=1))
            data= AccountUser()
            data.user_icon = form.cleaned_data['user_icon']
            data.birthday = form.cleaned_data['birthday']
            data.profile = form.cleaned_data['profile']
            data.sound_profile = form.cleaned_data['sound_profile']
            print(data.user_icon)


            # redirect to a new URL:
            return redirect('../mypage/', {"data":data})

        print("nonvalid")
        return render(request, 'accounts/profile.html',{"form":form})
