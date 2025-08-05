from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional

class AlumnoBase(BaseModel):
    nombre: str
    edad: int
    carrera: str

class AlumnoCreate(AlumnoBase):
    pass

class Alumno(AlumnoBase):
    id: UUID
