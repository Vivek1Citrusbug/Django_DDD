from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blogs.infrastructure.models import BlogPost
from ..application.forms import BlogPostForm
from blogs.application.services import BlogPostService


class BlogPostListingView(LoginRequiredMixin, ListView):
    template_name = "blogs/blog_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        service = BlogPostService()
        return service.list_posts()


class BlogDetailView(LoginRequiredMixin, DetailView):
    template_name = "blogs/blog_detail.html"
    context_object_name = "post"

    def get_object(self, **kwargs):
        service = BlogPostService()
        return service.get_post_details(kwargs["pk"])

class BlogCreateView(LoginRequiredMixin, CreateView):
    """Handles the creation of a new blog post."""

    form_class = BlogPostForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")

    def form_valid(self, form):
        # Use the service to handle blog creation
        blog_service = BlogPostService()
        blog_service.create_blog(
            author=self.request.user,
            title=form.cleaned_data["title"],
            content=form.cleaned_data["content"],
        )
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Handles updating an existing blog post."""

    form_class = BlogPostForm
    template_name = "blogs/blog_form.html"
    success_url = reverse_lazy("blog_list")

    def get_object(self, queryset=None):
        # Fetch the blog using the service
        blog_service = BlogPostService()
        return blog_service.get_blog_by_id(self.kwargs["pk"])

    def test_func(self):
        # Check if the current user is the blog's author
        blog_service = BlogPostService()
        blog = blog_service.get_blog_by_id(self.kwargs["pk"])
        return blog.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Handles deleting a blog post."""

    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blog_list")

    def get_object(self, queryset=None):
        # Fetch the blog using the service
        blog_service = BlogPostService()
        return blog_service.get_blog_by_id(self.kwargs["pk"])

    def test_func(self):
        # Check if the current user is the blog's author or staff
        blog_service = BlogPostService()
        blog = blog_service.get_blog_by_id(self.kwargs["pk"])
        return blog.author == self.request.user or self.request.user.is_staff
    
# class BlogPostListingView(LoginRequiredMixin, ListView):
#     """This view is used to list all the blogs"""

#     model = BlogPost
#     template_name = "blogs/blog_list.html"
#     context_object_name = "posts"
#     ordering = ["-date_published"]


# class BlogDetailView(LoginRequiredMixin, DetailView):
#     """This view is used to give detail of selected blog"""

#     model = BlogPost
#     template_name = "blogs/blog_detail.html"
#     context_object_name = "post"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.get_object()
#         context["likes_count"] = post.likes.count()
#         context["user_liked"] = post.likes.filter(
#             user=self.request.user
#         ).exists()  
#         return context


# class BlogCreateView(LoginRequiredMixin, CreateView):
#     """This view is used to create new blog"""

#     model = BlogPost
#     form_class = BlogPostForm
#     template_name = "blogs/blog_form.html"
#     success_url = reverse_lazy("blog_list")

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     """This view is used to update existing blog"""

#     model = BlogPost
#     form_class = BlogPostForm
#     template_name = "blogs/blog_form.html"
#     success_url = reverse_lazy("blog_list")

#     def test_func(self):
#         post = self.get_object()
#         return post.author == self.request.user


# class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     """This view is used to delete existing blog"""

#     model = BlogPost
#     template_name = "blogs/blog_confirm_delete.html"
#     success_url = reverse_lazy("blog_list")
#     context_object_name = "post"

#     def test_func(self):
#         post = self.get_object()
#         return post.author == self.request.user or self.request.user.is_staff
