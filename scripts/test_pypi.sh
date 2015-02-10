reset
./scripts/uninstall.sh
./scripts/install_pypi.sh
#cd ..
python examples/simple/manage.py test fobi
#cd scripts