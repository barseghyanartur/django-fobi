reset
./uninstall.sh
./install.sh
python examples/simple/manage.py test fobi --settings=settings_bootstrap3_theme_django17 --traceback -v 3
