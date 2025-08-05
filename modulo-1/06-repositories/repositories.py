from typing import List, Optional
from uuid import UUID, uuid4
from schemas import Alumno, AlumnoCreate

class AlumnoRepository:
    def __init__(self):
        self._alumnos: List[Alumno] = []

    def listar(self) -> List[Alumno]:
        return self._alumnos

    def obtener(self, alumno_id: UUID) -> Optional[Alumno]:
        return next((a for a in self._alumnos if a.id == alumno_id), None)

    def crear(self, data: AlumnoCreate) -> Alumno:
        nuevo = Alumno(id=uuid4(), **data.dict())
        self._alumnos.append(nuevo)
        return nuevo

    def actualizar(self, alumno_id: UUID, data: AlumnoCreate) -> Optional[Alumno]:
        alumno = self.obtener(alumno_id)
        if alumno:
            alumno.nombre = data.nombre
            alumno.edad = data.edad
            alumno.carrera = data.carrera
        return alumno

    def eliminar(self, alumno_id: UUID) -> bool:
        alumno = self.obtener(alumno_id)
        if alumno:
            self._alumnos.remove(alumno)
            return True
        return False
