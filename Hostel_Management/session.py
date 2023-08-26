""" Session Architecture """
import time

# Create a session class


class Session:
    def __init__(self, user):
        self.user = user
        self.creation_time = time.time()
        self.expiration_time = self.creation_time + (30 * 60)  # 30 minutes

    def is_valid(self):
        return time.time() < self.expiration_time
