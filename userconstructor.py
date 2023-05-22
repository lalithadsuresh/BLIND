class User:

    def __init__(self, username, password):
        self.likes = 0
        self.username = username
        self.password = password

    def display_info(self):
        ("username:", self.username)
        ("password:", self.password)

class SignUp:

    def __init__(self):
        self.users = []

    def registered_users(self, username, password):
        new_user = User(username, password)
        self.users.append(new_user)
        print("user registered")

    def displayed_users(self):
        size = len(self.users)
        print(size, "registered users:")
        for user in self.users:
            user.display_info()
        
    