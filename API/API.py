from Models import Post
import datetime
class API:
    def __init__(self, config=None):
        self.config = config
    def add_post(self, post: Post):
        # POST HTTP request to backend to add the post
        # Returns a list of Posts
        return [
            Post(
                "Adam", "Python is a snake",
                datetime.datetime(year=2021, month=5, day=1)
            ),
            Post(
                "Sara", "Python is a programming language",
                datetime.datetime(year=2021, month=5, day=3)
            )]