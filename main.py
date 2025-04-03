from pydantic import BaseModel


class Student(BaseModel):
    id: int
    name: str
    username: str
    email: str
    password: str
    school_id: int = 1


class School(BaseModel):
    id: int
    name: str
    email: str
    address: str
    class_room: int


student = {
    "id": 1,
    "name": "Anna",
    "username": "anna24",
    "email": "annna@gmail.com",
    "password": "qwert1234",
}

school = {
    "id": 1,
    "name": "PDP School",
    "email": "pdpschool@gmail.com",
    "address": "Tashkent",
    "class_room": 200,
}

stu = Student(**student)

sch = School(**school)

print(stu)
print(stu.username)
print(sch)
print(sch.address)
"""
id=1 name='Anna' username='anna24' email='annna@gmail.com' password='qwert1234' school_id=1
anna24
id=1 name='PDP School' email='pdpschool@gmail.com' address='Tashkent' class_room=200
Tashkent
"""
