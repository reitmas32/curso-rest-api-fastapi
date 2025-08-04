from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID

from schemas import Alumno, AlumnoCreate

router = APIRouter()

@router.get("/alumnos", response_model=List[Alumno])
def listar_alumnos():
    return []

@router.get("/alumnos/{alumno_id}", response_model=Alumno)
def obtener_alumno(alumno_id: UUID):
    alumno = [
        {
            "id": UUID("123e4567-e89b-12d3-a456-426614174000"),
            "nombre": "Juan Perez",
            "edad": 20,
            "carrera": "Ingenieria"
        }
    ]
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.post("/alumnos", response_model=Alumno)
def crear_alumno(data: AlumnoCreate):
    return {
        "id": UUID("123e4567-e89b-12d3-a456-426614174000"),
        "nombre": data.nombre,
        "edad": data.edad,
        "carrera": data.carrera
    }

@router.put("/alumnos/{alumno_id}", response_model=Alumno)
def actualizar_alumno(alumno_id: UUID, data: AlumnoCreate):
    alumno = [
        {
            "id": alumno_id,
            "nombre": data.nombre,
            "edad": data.edad,
            "carrera": data.carrera
        }
    ]
    if not alumno:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return alumno

@router.delete("/alumnos/{alumno_id}")
def eliminar_alumno(alumno_id: UUID):
    if not []:
        raise HTTPException(status_code=404, detail="Alumno no encontrado")
    return {"message": f"Alumno {alumno_id} eliminado"}
