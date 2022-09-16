from os import link
from re import A
from django.shortcuts import render, redirect
from django.views.generic import View
from requests import post
from .models import Post, AppComment, AppSeminar, AppSeminarParticipant
from .forms import PostForm, CommentForm, PostStudyForm, CommentStudyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import AccountUser
from deep_translator import GoogleTranslator

# インデックスを表示
class IndexView(View):
    def get(self, request, *args, **kwargs):
        item_name = request.GET.get('item_name')




        post_data = Post.objects.order_by('-id')

        if item_name != '' and item_name is not None:
            item_name = GoogleTranslator(source='auto', target='ja').translate(item_name)
            #print(item_name)
            post_data = Post.objects.filter(content__icontains=item_name)
        imgs = []
        for post in post_data:
            imgs.append(AccountUser.objects.get(id=post.author.id).user_icon)


        return render(request, 'app/index.html',  {
            'post_data': list(zip(post_data,imgs))
        })


class IndexStudyView(View):
    def get(self, request, *args, **kwargs):
        """自分の投稿と，フォローしているユーザーの投稿のみmを返す"""
        item_name = request.GET.get('item_name')
        post_data = AppSeminar.objects.order_by('-id')

        if item_name != '' and item_name is not None:
            item_name = GoogleTranslator(source='auto', target='ja').translate(item_name)
            #print(item_name)
            post_data = AppSeminar.objects.filter(content__icontains=item_name)

        return render(request, 'app/study_posts.html',  {
            'post_data': post_data
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        img = AccountUser.objects.get(id=post_data.author.id).user_icon
        

        #  コメントを表示
        if request.method == "POST":
            form = CommentForm(request.POST or None)
        else:
            form = CommentForm()


        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form,'img': img
        })
        
    def post(self, request, *args, **kwargs):
        post_data = PostForm(request.POST or None)

        #  コメントを表示
        if request.method == "POST":
            form = CommentForm(request.POST or None)
 
            if form.is_valid():
                comment = form.save(commit=False)
                comment.posted_id = kwargs['pk']
                comment.author = request.user
                comment.save()
                return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form
        })

# to do :  duplicate
class PostStudyDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        img = AccountUser.objects.get(id=post_data.author.id).user_icon
        

        #  コメントを表示
        if request.method == "POST":
            form = CommentForm(request.POST or None)
        else:
            form = CommentForm()

        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form, 'img': img
        })
        
    def post(self, request, *args, **kwargs):
        post_data = PostForm(request.POST or None)

        #  コメントを表示
        if request.method == "POST":
            form = CommentForm(request.POST or None)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.posted_id = kwargs['pk']
                comment.author = request.user
                comment.save()
                return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form
        })

#   勉強会の詳細
class PostStudyDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.get(id=self.kwargs['pk'])
        img = AccountUser.objects.get(id=post_data.author.id).user_icon
        
        #  コメントを表示
        if request.method == "POST":
            form = CommentStudyForm(request.POST or None)
        else:
            form = CommentStudyForm()

        return render(request, 'app/post_detail_study.html', {
            'post_data': post_data, 'form': form , 'img': img
        })
        
    def post(self, request, *args, **kwargs):
        post_data = PostStudyForm(request.POST or None)

        #  コメントを表示
        if request.method == "POST":
            form = CommentStudyForm(request.POST or None)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.posted_id = kwargs['pk']
                comment.author = request.user
                comment.save()
                return redirect('post_study_detail', self.kwargs['pk'])

        return render(request, 'app/post_detail_study.html', {
            'post_data': post_data, 'form': form
        })


#   タイムラインの投稿
class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        return render(request, 'app/post_form.html', {
            'form':form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', post_data.id)
        
        return render(request, 'app/post_form.html', {
            'form':form
        }) 

#  勉強会の投稿
class CreatePostStudyView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostStudyForm(request.POST or None)

        return render(request, 'app/post_form_study.html', {
            'form':form
        })

    def post(self, request, *args, **kwargs):
        form = PostStudyForm(request.POST or None)

        if form.is_valid():
            post_data = AppSeminar()
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.link = form.cleaned_data['link']
            post_data.save()
            return redirect('post_study_detail', post_data.id)
        
        return render(request, 'app/post_form_study.html', {
            'form':form
        })       

#   投稿の編集
class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'content': post_data.content
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])
        
        return render(request, 'app/post_form.html', {
            'form':form
        })   

#   投稿の削除
class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')

#   勉強会投稿の編集
class PostStudyEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.get(id=self.kwargs['pk'])
        form = PostStudyForm(
            request.POST or None,
            initial = {
                'title': post_data.title,
                'content': post_data.content,
                'link': post_data.link
            }
        )

        return render(request, 'app/post_form_study.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = PostStudyForm(request.POST or None)

        if form.is_valid():
            post_data = AppSeminar.objects.get(id=self.kwargs['pk'])
            post_data.author = request.user
            post_data.title = form.cleaned_data['title']
            post_data.content = form.cleaned_data['content']
            post_data.save()
            return redirect('post_study_detail', self.kwargs['pk'])
        
        return render(request, 'app/post_form_study.html', {
            'form':form
        })   

#   勉強会投稿の削除
class PostStudyDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_study_delete.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')


#   リンクの詳細
class PostStudyLinkView(View):
    def get(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.get(id=self.kwargs['pk'])

        participate_data = AppSeminarParticipant()
        participate_data.user = request.user
        participate_data.seminar = AppSeminar.objects.get(id=self.kwargs['pk'])
        participate_data.save()

        return render(request, 'app/post_detail_study_link.html', {
            'post_data': post_data
        })

    def post(self, request, *args, **kwargs):
        post_data = AppSeminarParticipant()
        post_data.user = request.user
        post_data.seminar = AppSeminar.objects.get(id=self.kwargs['pk'])
        post_data.save()

        return redirect('post_detail', self.kwargs['pk'])