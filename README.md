# CRUD

Creación de un crud para carga de alumnos

1.- Se debe crear un ambiente virtual de python

``python -m venv .venv``

2.- Se debe activar el ambiente virtual

``cd .venv\Scripts``

``.\activate``

una vez activado en la consola debe aparecer al inicio de la ruta (.venv)

se debe volver a la carpeta raiz

``cd ../..``

3.- Se deben instalar las dependencias que aparecen en requirements.txt.

`` pip install -r requirements.txt``

puede que python solicite actualizar pip, en tal caso se debe actualizar con

``python.exe -m pip install --upgrade pip``

luego ejecutar de nuevo

`` pip install -r requirements.txt``

4.- Para crear el ejecutable bien sea desde Windows, linux o mac, se debe ejecutar

``pyinstaller --onefile .\main.py``
