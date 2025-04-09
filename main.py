from fastapi import FastAPI, APIRouter
from model import School, Student
from data import school_db, student_db

app = FastAPI()

router = APIRouter(
    prefix="/api"
)

school_data: dict = {}
student_data: dict = {}


# http://127.0.0.1:8000/api/school
@router.get("/school")
async def school():
    return {"data": school_db}


@router.get("/student")
async def student():
    return {"data": student_db}


@router.post("/school")
async def school_create(schools: School):
    school_data["title"] = schools.title
    school_data["room"] = schools.room
    school_data["teacher"] = schools.teacher

    return {"data": school_data}


@router.post("/student")
async def student_create(students: Student):
    school_data["name"] = students.name
    school_data["email"] = students.email
    school_data["room_id"] = students.room_id
    school_data["since"] = students.since
    return {"data": school_data}


app.include_router(router)
