from fastapi import APIRouter, HTTPException, BackgroundTasks
from scripts.handlers.user_handlers import UserHandler
from scripts.schema.user_schema import LoginRequest
from celery_app import bg1_celery

user_service = APIRouter(prefix="/user", tags=["User"])

@bg1_celery.task
def bg_task():
    print("background task")

# @user_service.post("/login")
# async def user_login(login: LoginRequest, background_task: BackgroundTasks):
#     background_task.add_task(bg_task)
#     print("pushed bg_task to background")
#     return await UserHandler().user_login(login)

@user_service.post("/login")
async def user_login(login: LoginRequest):
    bg_task.delay()
    print("pushed bg_task to background")
    return await UserHandler().user_login(login)
