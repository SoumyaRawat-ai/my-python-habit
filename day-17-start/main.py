class User:
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.following +=1
        self.followers +=1

user_1 = User("001", "Soumya")


print(user_1.username, user_1.id, user_1.followers)


user_2 = User("002", "Angila")

print(user_2.id, user_2.username)
user_1.follow(user_2)
print(user_2.following, user_2.followers, user_1.following, user_1.followers)