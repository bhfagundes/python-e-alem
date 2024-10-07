from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_all_users(self):
        return self.user_repository.get_all_users()