# build_files.sh
echo "Instalando requerimientos..."
pip install -r requirements.txt

# Automatic migrations
#echo "Iniciando migraciones..."
#python manage.py makemigrations && python manage.py migrate

# Colecta de staticsFiles en theme/static/
echo "Colectando StaticFiles..."
python3.9 manage.py collectstatic --noinput
