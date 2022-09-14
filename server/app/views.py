from django.shortcuts import render, redirect
from django.views.generic import View
from requests import post
from .models import Post, AppComment, AppSeminar
from .forms import PostForm, CommentForm, PostStudyForm, CommentStudyForm
from django.contrib.auth.mixins import LoginRequiredMixin

# インデックスを表示
class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html',  {
            'post_data': post_data
        })

class IndexStudyView(View):
    def get(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.order_by('-id')
        return render(request, 'app/study_posts.html',  {
            'post_data': post_data
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        

        #  コメントを表示
        if request.method == "POST":
            form = CommentForm(request.POST or None)
        else:
            form = CommentForm()

        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form
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
        
        #  コメントを表示
        if request.method == "POST":
            form = CommentStudyForm(request.POST or None)
        else:
            form = CommentStudyForm()

        return render(request, 'app/post_detail_study.html', {
            'post_data': post_data, 'form': form
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
            return redirect('post_detail', post_data.id)
        
        return render(request, 'app/post_form_study.html', {
            'form':form
        })       


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

class PostStudyLinkView(View):
    def get(self, request, *args, **kwargs):
        post_data = AppSeminar.objects.get(id=self.kwargs['pk'])
        
        return render(request, 'app/post_detail_study_link.html', {
            'post_data': post_data,
        })
        