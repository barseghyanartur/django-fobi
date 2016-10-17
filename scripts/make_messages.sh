echo 'Making messages for django-fobi...'
cd src/fobi/
#django-admin.py makemessages -l hy
django-admin.py makemessages -l de
django-admin.py makemessages -l nl
django-admin.py makemessages -l ru

echo 'Making messages for example projects...'
cd ../../examples/simple/
#django-admin.py makemessages -l hy
django-admin.py makemessages -l de
django-admin.py makemessages -l nl
django-admin.py makemessages -l ru
