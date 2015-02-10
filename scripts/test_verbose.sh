reset
./scripts/uninstall.sh
./scripts/install.sh
#cd ..
python examples/simple/manage.py test fobi --traceback
#cd scripts