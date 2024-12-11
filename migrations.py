from models.user import Base
from config.database import engine

# Tạo bảng trong database
print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")