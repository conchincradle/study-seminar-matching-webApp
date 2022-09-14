from django.shortcuts import render, redirect
from django.views.generic import View
from requests import post
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

# インデックスを表示
class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html',  {
            'post_data': post_data
        })

class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        

        #  コメントを表示
        if request.method == "POST":
            form = CommentForm(request.POST or None)

            # if form.is_valid():
            #     comment = form.save(commit=False)
            #     comment.posted_id = post_data
            #     comment.save()
                
            #     return redirect('post_detail', self.kwargs['pk'])
        
        else:
            form = CommentForm()

        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form
        })
        
    def post(self, request, *args, **kwargs):
        post_data = PostForm(request.POST or None)
        form = CommentForm(request.POST or None)
        import pprint
        pprint.pprint('aaaaaaaaaaaa')

        if form.is_valid():
            comment = form.save(commit=False)
            print(request.user)


            #comment.posted_id = 321
            import pprint
            pprint.pprint(vars(request))
            pprint.pprint(vars(comment))
            """
            {'_state': <django.db.models.base.ModelState object at 0x7f8edb078430>,
            'author_id': None,
            'content': 'aaaa',
            'created': datetime.datetime(2022, 9, 14, 2, 9, 4, 950662, tzinfo=<UTC>),
            'id': None,
            'posted_id_id': None}
            """
            comment.save()
            return redirect('post_detail', self.kwargs['pk'])

        return render(request, 'app/post_detail.html', {
            'post_data': post_data, 'form': form
        })

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