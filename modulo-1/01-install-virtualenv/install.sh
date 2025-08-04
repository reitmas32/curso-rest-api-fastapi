#!/bin/bash

echo "🔧 Instalando virtualenv..."
pip install --user virtualenv

echo "📦 Creando entorno virtual 'my-env'..."
python3 -m virtualenv my-env

# Paso 3: Activar entorno virtual
echo "⚙️ Activando entorno virtual..."
source my-env/bin/activate

# Paso 4: Instalar FastAPI y Uvicorn
echo "📥 Instalando FastAPI y Uvicorn..."
pip install fastapi uvicorn

# Paso 5: Confirmar instalación
echo "✅ Instalación completada."
echo "🎯 Puedes iniciar tu servidor con:"
echo "    uvicorn main:app --reload"

# Mantener el entorno activo si estás en un shell interactivo
$SHELL
