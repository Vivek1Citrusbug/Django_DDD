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
        return self.get_repo().all()
    # filter(post_id=post).order_by("-date_posted")

    
