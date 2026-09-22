from database import Base,engine,SessionLocal
from models import User
from data import users
from auth import get_password_hash

Base.metadata.create_all(bind=engine)
db=SessionLocal()
try:
    db.query(User).delete()
    for user_data in users:
        user=User(
            username=user_data['username'],
            email=user_data['email'],
            password_hash=get_password_hash(user_data['password']),
            role=user_data['role']
        )
        db.add(user)
        db.commit()
finally:
    db.close()