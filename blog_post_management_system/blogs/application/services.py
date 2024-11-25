from ..domain.repositories import BlogPostRepository


class BlogPostService:
    """Application service for blog post use cases"""

    def __init__(self, blog_post_repo: BlogPostRepository):
        self.blog_post_repo = blog_post_repo

    def list_posts(self):
        return self.blog_post_repo.get_all_posts()

    def get_post_details(self, post_id):
        return self.blog_post_repo.get_post_by_id(post_id)

    def create_post(self, title, content, author):
        post = self.blog_post_repo.model(
            title=title, content=content, author=author
        )
        self.blog_post_repo.save_post(post)

    def delete_post(self, post_id):
        self.blog_post_repo.delete_post(post_id)
