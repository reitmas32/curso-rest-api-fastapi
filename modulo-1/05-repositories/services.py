from typing import List, Optional
from schemas import Alumno, AlumnoCreate
from repositories import AlumnoRepository
from uuid import UUID

class AlumnoService:
    def __init__(self, repo: AlumnoRepository):
        self.repo = repo

    def listar(self) -> List[Alumno]:
        return self.repo.listar()

    def obtener(self, alumno_id: UUID) -> Optional[Alumno]:
        return self.repo.obtener(alumno_id)

    def crear(self, data: AlumnoCreate) -> Alumno:
        return self.repo.crear(data)

    def actualizar(self, alumno_id: UUID, data: AlumnoCreate) -> Optional[Alumno]:
        return self.repo.actualizar(alumno_id, data)

    def eliminar(self, alumno_id: UUID) -> bool:
        return self.repo.eliminar(alumno_id)
