reset
./scripts/uninstall.sh
./scripts/install_python_3.sh
python examples/simple/manage.py test fobi --traceback --settings=settings.bootstrap3_theme_python_3_django_1_8 --traceback -v 3
