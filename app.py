from fastapi import FastAPI
from controllers import user_controller

app = FastAPI()

# Đăng ký router
app.include_router(user_controller.router, prefix="/api", tags=["users"])

# Điểm kiểm tra
@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management API"}