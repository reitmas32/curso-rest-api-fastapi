# Diseño Limpio de APIs REST con FastAPI

Este repositorio contiene los materiales, código fuente y ejemplos desarrollados durante el curso **Diseño Limpio de APIs REST con FastAPI**. El objetivo es capacitarte en la creación de APIs modernas, robustas y mantenibles, siguiendo principios de arquitectura limpia y buenas prácticas de desarrollo backend.

---

## 🎯 Objetivo general

Desarrollar APIs Web modernas utilizando **FastAPI**, incorporando:

- Validación de datos con **Pydantic**
- Pruebas automatizadas con **Pytest**
- Acceso a bases de datos con **SQLAlchemy (async)**
- Principios de **arquitectura hexagonal**
- Despliegue para producción

---

## 🧠 Contenido del curso

### Módulo 1: Introducción a FastAPI y Pydantic
- Instalación del entorno
- ¿Qué es ASGI? ¿Por qué `async def`?
- Rutas y validación de datos
- Documentación automática (`/docs`)

### Módulo 2: Manejo de errores, dependencias y pruebas
- HTTPException y personalización de respuestas
- `Depends()` para servicios y autenticación
- Introducción a **Pytest** y **TestClient**

### Módulo 3: CRUD y base de datos
- SQLAlchemy asincrónico
- Modelos y migraciones
- Middleware y testing con base de datos

### Módulo 4: Despliegue y arquitectura hexagonal
- `.env`, estructura, Git y Docker
- Fundamentos de Hexagonal: Puertos y Adaptadores

### Módulo 5: Proyecto final y buenas prácticas
- Refactor a estructura hexagonal
- Interfaces, desacoplamiento y Zen de Python
- Proyecto integrador y recursos adicionales

---

## 🔧 Requisitos del curso

- Conocimientos intermedios de **Python**
- Recomendable: nociones básicas de **Git**

---

## ⚙️ Instalación rápida

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
