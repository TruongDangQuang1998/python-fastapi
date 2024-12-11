from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from services.user_service import UserService
from config.database import get_db
from pydantic import BaseModel

router = APIRouter()
# Tạo class User để mô tả dữ liệu trả về
class User(BaseModel):
    id: int
    name: str 
    email: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "id": 1,
                "email": "johndoe@example.com"
            }
        }

# Model cho Request Body
class UserCreate(BaseModel):
    name: str 
    email: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com"
            }
        }
@router.get("/users/{user_id}",response_model=User)
def get_user(user_id : int = Path(..., example=123) , db: Session = Depends(get_db)):
    return UserService.get_user(db, user_id)

@router.post("/users")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user_data_dict = dict(
        name = user_data.name,
        email = user_data.email
    )
    return UserService.create_user(db, user_data_dict)

@router.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(db, user_id)