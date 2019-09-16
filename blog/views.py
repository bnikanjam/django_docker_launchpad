from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Review
from django.utils import timezone


class PostCreateView(CreateView):
    model = Post
    # context_object_name = 'form'
    template_name = 'blog/post_create.html'
    fields = ['title', 'content',]
    success_url = '/blog/'

    # Set author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostListView(ListView):
    """A page representing a list of posts"""
    queryset = Post.objects.all()
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostDetailView(DetailView):
    """A page representing one post"""
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostUpdateView(UpdateView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
