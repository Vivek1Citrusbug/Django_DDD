from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, RedirectView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from comments.domain.models import UserComments
from blogs.domain.models import BlogPost
from comments.application.forms import CommentForm
from django.shortcuts import get_object_or_404
from blogs.application.services import BlogPostAppService
from comments.application.services import CommentAppService

class CommentListView(LoginRequiredMixin, ListView):
    """This view is used to list user comments"""

    model = UserComments
    template_name = "comments/list_comments.html"
    context_object_name = "comments"
    # services: CommentAppService

    def get_queryset(self):
        # post = get_object_or_404(BlogPost, pk=self.kwargs["pk"])
       
        PostsService = BlogPostAppService()
        post = PostsService.get_post_details(self.kwargs["pk"]) 
        CommentService = CommentAppService()
        print("post printed : ",post)
        return CommentService.get_comments_application(post)
        # return UserComments.objects.filter(post_id=post).order_by("-date_posted")
        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        PostService = BlogPostAppService()
        context["post"] = PostService.get_post_details(post_id=self.kwargs["pk"])
        # context["post"] = BlogPost.objects.get(id=self.kwargs["pk"])
        # print("context post printed : ",context["post"])
        return context
        
        


class CommentCreateView(LoginRequiredMixin, CreateView):
    """This view is used to create new user comments"""

    model = UserComments
    template_name = "comments/create_comment.html"
    form_class = CommentForm
    # service = BlogPostAppService()

    def form_valid(self, form):
        PostService = BlogPostAppService()
        post = PostService.get_post_details(post_id=self.kwargs["pk"])
        form.instance.user_id = self.request.user
        form.instance.post_id = post

        # form.instance.post_id = BlogPost.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("list_comment", kwargs={"pk": self.kwargs["pk"]})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """This view is used to delete user comments"""

    model = UserComments
    template_name = "comments/delete_comment.html"

    def get_success_url(self):
        return reverse_lazy("list_comment", kwargs={"pk": self.object.post_id.pk})

    def test_func(self):
        """
        Ensure only the comment's author or admin can delete the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.user_id or self.request.user.is_staff or self.request.user == comment.post_id.author
