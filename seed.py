from app import app
from models import User, Admin, Meal, Transaction, Category,db
from faker import Faker
if __name__ == '__main__':
    fake=Faker()
    with app.app_context():
        db.drop_all()
        db.create_all()

        users=[]

        for i in range(10):
            user = User(
                username=fake.name(),
                email=fake.email(),
                password=fake.password(length=16),
                role='user'
            )
            users.append(user)

        for i in range(5):
            user = User(
                username=fake.name(),
                email=fake.email(),
                password=fake.password(length=16),
                role='admin'
            )
            users.append(user)

        db.session.add_all(users)
        db.session.commit()
        print('Seeded users')