./scripts/uninstall.sh
./scripts/install.sh
cat README.rst SCREENSHOTS.rst docs/documentation.rst.distrib > docs/index.rst
cat QUICK_START.rst > docs/quickstart.rst
sphinx-build -n -a -b html docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

