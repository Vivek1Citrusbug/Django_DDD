from ..domain.repositories import BlogPostRepository
from .models import BlogPost,BlogPostFactory

class BlogPostService:
    """Domain service for blog post use cases"""

    @staticmethod
    def get_repo():
        return BlogPost.objects
    
    @staticmethod
    def get_factory():
        return BlogPostFactory
    
    def get_post_by_id(self, post_id):
        """Retrieve a single post by its ID."""
        
        try:
            return self.get_repo().get(id=post_id)
        except BlogPost.DoesNotExist:
            return None

    def list_posts(self):
        """Retrieve all blog posts."""

        return self.get_repo().all()

    def create_post_domain(self, title, content, author):
        """Create a new blog post."""
        post = self.get_factory().create_blog_factory(title,content,author)
        post.save()
        return post

    def delete_post_domain(self, post_id):
        """Delete a blog post by ID."""

        try:
            post = self.get_repo().get(id=post_id)
            post.delete()
            return True
        except BlogPost.DoesNotExist:
            return False


        
    



    
