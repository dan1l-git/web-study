from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from configuration import Configuration

settings = Configuration()

user = settings.POSTGRES_USER
password = settings.POSTGRES_PASSWORD
host = settings.POSTGRES_HOST
db_name = settings.POSTGRES_DB

DATABASE_URL = f"postgresql://{user}:{password}@{host}:5432/{db_name}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()