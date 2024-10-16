import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from scripts.services.user_services import user_service
from scripts.utils.custom_exceptions import CustomException

app = FastAPI()

app.include_router(user_service)

@app.get("/")
def home(name: str):
    return name + "This is Home page"
@app.get("/{id}")
def get_id(id: str, name: str):
    return "Id is "+ str(id) + 'name is' + name

@app.exception_handler(CustomException)
async def custom_exception(request, exc):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"name": exc.name, "details": exc.desc}
    )

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=7000, reload=False )