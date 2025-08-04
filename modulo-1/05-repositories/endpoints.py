from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID

from schemas import Alumno, AlumnoCreate
from repositories import AlumnoRepository
from services import AlumnoService

router = APIRouter()
repo = AlumnoRepository()
service = AlumnoService(repo)

@router.get("/alumnos", response_model=List[Alumno])
def listar_alumnos():
    return service.listar()

@router.get("/alumnos/{alumno_id}", response_model=Alumno)
def obtener_alumno(alumno_id: UUID):
    alumno = service.obtener(alumno_id)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.post("/alumnos", response_model=Alumno)
def crear_alumno(data: AlumnoCreate):
    return service.crear(data)

@router.put("/alumnos/{alumno_id}", response_model=Alumno)
def actualizar_alumno(alumno_id: UUID, data: AlumnoCreate):
    alumno = service.actualizar(alumno_id, data)
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.delete("/alumnos/{alumno_id}")
def eliminar_alumno(alumno_id: UUID):
    if not service.eliminar(alumno_id):
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {"message": "Alumno eliminado"}
