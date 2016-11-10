echo 'Making messages for django-fobi...'
cd examples/simple/
./manage.py makemigrations fobi

echo 'Making messages for example projects...'
./manage.py makemigrations

echo 'Applying migrations...'
./manage.py migrate
