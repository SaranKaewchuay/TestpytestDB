from pydantic import BaseModel

class Courses(BaseModel):
    course_code: str
    course_name: str
    year: int
    group : int 
    number : int 
    