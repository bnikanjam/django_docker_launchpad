from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Review
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # context_object_name = 'form'
    template_name = 'blog/post_create.html'
    fields = ['title', 'content',]
    success_url = '/blog/'

    # Set author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ['title', 'content']

    # set author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    # Is current post author same as logged-in user?
    #
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(DeleteView):
    """A view that displays a confirmation page and deletes an existing object. The given object will only be deleted
    if the request method is POST. If this view is fetched via GET, it will display a confirmation page that should
    contain a form that POSTs to the same URL. """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/blog/'

    # make sure current post author is same as logged-in user
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
