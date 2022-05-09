Primero se debe crear el entorno virtual en la carpeta donde se va crear el Backend
EL entorno virtuak puede uedar en cualquier parte de su computador, pero es necesario que sepan donde esta para poder acrivarlo y correr el poyecto

ejecutar 
python -m venv %nombre carpeta%

Si sale el error de que no puede ejecutar scripts ejecutar

Get-ExecutionPolicy

Si sale Restricted ejecutar

Set-ExecutionPolicy Unrestricted

Posteriormente ejecutar

.\activate

Ejecutar en la ruta donde está el backend, es decir salirse hasta donde esta la carpeta creada del venv
pip install Django

pip install -r requirements.txt

python manage.py migrate //para activar el proyecto 
python manage.py runserver
