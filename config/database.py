from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5433/sqlalchemy_codefirst"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Dependency get session in services
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()