from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository

class UserService:
    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserRepository.get_user_by_id(db, user_id)
    
    @staticmethod
    def create_user(db: Session, user_data: dict):
        return UserRepository.create_user(db, user_data)
    
    @staticmethod
    def delete_user(db: Session, user_id: int):
        return UserRepository.delete_user(db, user_id)