from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Review


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'post_list'
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        return context


class PostCreateView(CreateView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post


class PostDeleteView(DeleteView):
    pass


class ReviewDetailView(DetailView):
    pass


class ReviewListView(ListView):
    pass


class ReviewCreateView(CreateView):
    pass


class ReviewUpdateView(UpdateView):
    pass


class ReviewDeleteView(DeleteView):
    pass
