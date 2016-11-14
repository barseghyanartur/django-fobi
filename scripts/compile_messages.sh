echo 'Compiling messages for django-fobi...'
cd src/fobi/
#django-admin.py compilemessages -l hy
django-admin.py compilemessages -l de
django-admin.py compilemessages -l nl
django-admin.py compilemessages -l ru

echo 'Compiling messages for example projects...'
cd ../../examples/simple/
#django-admin.py compilemessages -l hy
django-admin.py compilemessages -l de
django-admin.py compilemessages -l nl
django-admin.py compilemessages -l ru
