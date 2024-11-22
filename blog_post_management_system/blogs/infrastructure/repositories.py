# post/infrastructure/repositories.py
from models import BlogPost

class BlogPostRepository:
    @staticmethod
    def get_post_by_id(post_id):
        return BlogPost.objects.get(id=post_id)

    @staticmethod
    def save_post(post):
        post.save()
