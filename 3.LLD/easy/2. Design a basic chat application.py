import time


class Messages:
    def __init__(self, id, content, username):
        self.id = id
        self.user = username
        self.content = content
        self.timing = time.now()


class ChatApplication:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.board = []
        self.id_to_message = {}

    def send(self, user, message):
        self.board.append(message)
