from ..domain.repositories import BlogPostRepository
from ..domain.services import BlogPostService

class BlogPostAppService:
    """Application service for blog post use cases"""

    def __init__(self):
        """Initialize domain service"""

        self.service = BlogPostService()

    def list_posts_application(self):
        """Access domain service for listing all posts"""

        return self.service.list_posts_instance()

    def get_post_details_application(self, post_id):
        """Access domain service for accessing specific post"""

        return self.service.get_post_by_id_instance(post_id)

    def create_post_application(self, title, content, author):
        """Access domain service for creating post"""

        post = self.service.create_post_instance(title=title, content=content, author=author)
        return post

    def delete_post_application(self, post_id):
        """Access domain service for deleting post"""

        self.service.delete_post_instance(post_id)
