#!/bin/sh
set -e

# ============================================================
# entrypoint.sh | Se ejecuta cada vez que arranca el contenedor "web"
# IMPORTANTE: este archivo debe guardarse con saltos de linea LF (Unix),
# no CRLF (Windows). Si lo editan con Notepad y lo guardan mal,
# el contenedor va a fallar con un error tipo "bad interpreter".
# Usen VS Code (abajo a la derecha, cambiar de CRLF a LF) o Notepad++.
# ============================================================

set -e

echo ">> Esperando a que la base de datos este lista..."

while ! python -c "import socket; s = socket.socket(); s.connect(('db', 5432)); s.close()"; do
    echo ">> Base de datos no disponible todavia, reintentando en 2s..."
    sleep 2
done

echo ">> Base de datos lista. Aplicando migraciones..."
python manage.py migrate --noinput

echo ">> Arrancando servidor..."
exec "$@"