from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///./database.db"


engine = create_engine(DATABASE_URL, echo=True, future=True)

SessionLocal =sessionmaker(
   bind=engine,
   expire_on_commit=False,
)
Base=declarative_base()