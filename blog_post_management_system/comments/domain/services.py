from comments.domain.models import UserComments
from django.shortcuts import get_object_or_404

class CommentDomainService:
    """Domain service for comment use cases"""

    @staticmethod
    def get_repo():
        return UserComments.objects

    def get_comment_domain(self,post):
        print("In Domain layer : ",post)
        # get_object_or_404(BlogPost, pk=self.kwargs["pk"])
        return self.get_repo().filter(post_id = post).order_by("-date_posted")

    def delete_comment_instance(self,commentObj,currentUser):
        # self.request.user == comment.user_id or self.request.user.is_staff or self.request.user == comment.post_id.author
        return currentUser == commentObj.user_id or currentUser.is_staff or currentUser == commentObj.post_id.author