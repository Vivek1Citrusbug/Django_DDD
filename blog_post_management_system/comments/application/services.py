from comments.domain.services import CommentDomainService

class CommentAppService:
    def __init__(self):
        """Initialize domain service"""

        self.service = CommentDomainService()

    def get_comments_application(self,post):
        """Service to get comments by post id"""
        print("In application layer : ",post)
        self.service.get_comment_domain(post)
