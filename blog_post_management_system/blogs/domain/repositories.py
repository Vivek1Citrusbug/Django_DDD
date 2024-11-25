from abc import ABC, abstractmethod


class BlogPostRepository(ABC):
    """Interface for blog post repository"""

    @abstractmethod
    def get_all_posts(self):
        pass

    @abstractmethod
    def get_post_by_id(self, post_id):
        pass

    @abstractmethod
    def save_post(self, post):
        pass

    @abstractmethod
    def delete_post(self, post_id):
        pass
