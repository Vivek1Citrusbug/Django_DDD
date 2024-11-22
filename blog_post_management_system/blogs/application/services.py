# post/application/services.py
from blogs.infrastructure.models import BlogPost

class BlogPostService:
    @staticmethod
    def get_likes_count(post):
        return post.likes.count()

    @staticmethod
    def user_liked_post(post, user):
        return post.likes.filter(user=user).exists()

    @staticmethod
    def create_blog_post(title, content, author):
        post = BlogPost.objects.create(
            title=title, content=content, author=author
        )
        return post
