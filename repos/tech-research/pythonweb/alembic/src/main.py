from sqlmodel import Session
from database import engine
from models import User, Post

def create_sample_data():
    with Session(engine) as session:
        user = User(name="Alice", email="alice@example.com")
        session.add(user)
        session.commit()

        post = Post(title="First Post", content="Hello World!", user_id=user.id)
        session.add(post)
        session.commit()

def fetch_data():
    with Session(engine) as session:
        users = session.exec(User.select()).all()
        posts = session.exec(Post.select()).all()

        print("\n📌 Users:")
        for user in users:
            print(user)

        print("\n📌 Posts:")
        for post in posts:
            print(post)

if __name__ == "__main__":
    create_sample_data()
    fetch_data()