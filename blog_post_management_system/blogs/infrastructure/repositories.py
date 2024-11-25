from ..domain.repositories import BlogPostRepository
from domain.models import BlogPost


class DjangoBlogPostRepository(BlogPostRepository):
    """Implementation of BlogPostRepository using Django ORM"""

    def get_all_posts(self):
        return BlogPost.objects.all()

    def get_post_by_id(self, post_id):
        return BlogPost.objects.filter(id=post_id).first()

    def save_post(self, post):
        post.save()

    def delete_post(self, post_id):
        BlogPost.objects.filter(id=post_id).delete()
