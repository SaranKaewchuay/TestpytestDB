from fastapi import APIRouter

from models.course_model import Courses
from config.database import collection_name

from schemas.course_schema import courses_serializer
from bson import ObjectId

course_api_router = APIRouter()

@course_api_router.get("/hello")
async def get_hello():
    return {"msg":"Hello World"}


# retrieve
@course_api_router.get("/")
async def get_courses():
    courses = courses_serializer(collection_name.find())
    return {"status":"ok","data": courses}

@course_api_router.get("/{id}")
async def get_course(id: str):
    course =  courses_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status":"ok","data": course}

# post
@course_api_router.post("/")
async def create_course(course: Courses):
    _id = collection_name.insert_one(dict(course))
    course = courses_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status":"ok","data": course}

# update
@course_api_router.put("/{id}")
async def update_course(id: str, course: Courses):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(course)
    })
    course = courses_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status":"ok","data": course}

# delete
@course_api_router.delete("/{id}")
async def delete_course(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}