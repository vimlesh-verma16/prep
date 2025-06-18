from datetime import datetime
import uuid
from collections import defaultdict


class User:
    def __init__(self, username, email):
        self.id = uuid.uuid4()
        self.username = username
        self.email = email
        self.reputation = 0

    def __str__(self):
        return f"{self.username} ({self.reputation} pts)"


class Tag:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name


class Comment:
    def __init__(self, content, author):
        self.id = uuid.uuid4()
        self.content = content
        self.author = author
        self.timestamp = datetime.now()


class Vote:
    UPVOTE = 1
    DOWNVOTE = -1

    def __init__(self, user, vote_type):
        self.user = user
        self.vote_type = vote_type


class Answer:
    def __init__(self, content, author, question):
        self.id = uuid.uuid4()
        self.content = content
        self.author = author
        self.question = question
        self.comments = []
        self.votes = []
        self.timestamp = datetime.now()

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_vote(self, vote):
        self.votes.append(vote)
        self.author.reputation += vote.vote_type

    def get_score(self):
        return sum(v.vote_type for v in self.votes)


class Question:
    def __init__(self, title, content, author, tags=None):
        self.id = uuid.uuid4()
        self.title = title
        self.content = content
        self.author = author
        self.answers = []
        self.comments = []
        self.tags = tags if tags else []
        self.votes = []
        self.timestamp = datetime.now()

    def add_answer(self, answer):
        self.answers.append(answer)

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_vote(self, vote):
        self.votes.append(vote)
        self.author.reputation += vote.vote_type

    def get_score(self):
        return sum(v.vote_type for v in self.votes)


class StackOverflow:
    def __init__(self):
        self.users = []
        self.questions = []
        self.tags = {}

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def post_question(self, title, content, author, tag_names):
        tags = [self._get_or_create_tag(name) for name in tag_names]
        question = Question(title, content, author, tags)
        self.questions.append(question)
        return question

    def post_answer(self, question, content, author):
        answer = Answer(content, author, question)
        question.add_answer(answer)
        return answer

    def post_comment(self, post, content, author):
        comment = Comment(content, author)
        post.add_comment(comment)
        return comment

    def vote(self, post, user, vote_type):
        vote = Vote(user, vote_type)
        post.add_vote(vote)

    def search_by_keyword(self, keyword):
        return [
            q
            for q in self.questions
            if keyword.lower() in q.title.lower()
            or keyword.lower() in q.content.lower()
        ]

    def search_by_tag(self, tag_name):
        return [q for q in self.questions if any(t.name == tag_name for t in q.tags)]

    def search_by_user(self, username):
        return [q for q in self.questions if q.author.username == username]

    def _get_or_create_tag(self, name):
        if name not in self.tags:
            self.tags[name] = Tag(name)
        return self.tags[name]


# Demo class for usage
class StackOverflowDemo:
    @staticmethod
    def run():
        so = StackOverflow()
        user1 = so.create_user("Alice", "alice@example.com")
        user2 = so.create_user("Bob", "bob@example.com")

        q1 = so.post_question(
            "How to write Python code?",
            "I'm new to Python...",
            user1,
            ["python", "beginner"],
        )
        a1 = so.post_answer(q1, "You should start with tutorials!", user2)

        so.post_comment(q1, "Good question!", user2)
        so.post_comment(a1, "Nice answer!", user1)

        so.vote(q1, user2, Vote.UPVOTE)
        so.vote(a1, user1, Vote.UPVOTE)

        print("Search by keyword 'Python':")
        for q in so.search_by_keyword("Python"):
            print(f"{q.title} - Score: {q.get_score()}")

        print("\nReputation:")
        print(user1)
        print(user2)


# Run demo
if __name__ == "__main__":
    StackOverflowDemo.run()
