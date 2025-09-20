# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Database URL
# For SQLite file-based DB (app.db in project root). Replace with Postgres/MySQL later.
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# 2. Engine (actual DB connection)
# connect_args is only for SQLite, remove if using Postgres/MySQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. SessionLocal (factory to create new DB sessions per request)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base class for all ORM models
Base = declarative_base()

# 5. Dependency for FastAPI routes (injects DB session, closes after request)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
