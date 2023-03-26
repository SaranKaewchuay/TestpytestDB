def course_serializer(course) -> dict:
    return {
        "id": str(course["_id"]),
        "course_code": str(course["course_code"]),
        "course_name": str(course["course_name"]),
        "year": int(course["year"]),
        "group": int(course["group"]),
        "number": int(course["number"]),
    }
 

def courses_serializer(courses) -> list:
    return [course_serializer(course) for course in courses]