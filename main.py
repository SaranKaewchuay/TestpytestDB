from fastapi import FastAPI
from routes.courses_route import course_api_router

app = FastAPI()

app.include_router(course_api_router)

