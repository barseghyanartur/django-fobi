reset
./scripts/uninstall.sh
./scripts/install_python_3.sh
#cd ..
python examples/simple/manage.py test fobi --traceback
#cd scripts