from scripts.schema.user_schema import LoginRequest
from scripts.utils.custom_exceptions import CustomException
import time
from fastapi import HTTPException

class UserHandler():
    
    async def user_login(self, login: LoginRequest):
        try:
            time.sleep(4)
            return {"name": login.username}
            # raise HTTPException(status_code=401, detail="UnAuthorized")
            # raise CustomException(name="User", desc="Login Error")
        except Exception as error:
            print("Error in user login handler", error)
            raise error