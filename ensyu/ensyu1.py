# -*- coding: utf-8 -*-


class Students:
    def __init__(self, score):
        self.score = score


aa = Students({"english": 99 ,"math" :49})
print(aa.score)


class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def get_userinfo(self):
        print(self.user_id)
        print(self.username)
        print(self.email)


user1 = User(1, "okada", "okada@email.com")
user2 = User(2, "yamada", "yamada@email.com")
user1.get_userinfo()
user2.get_userinfo()

