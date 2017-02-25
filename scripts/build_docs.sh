#./scripts/uninstall.sh
#./scripts/install.sh
cat README.rst docs/screenshots.rst.distrib docs/documentation.rst.distrib > docs/index.rst
cat QUICK_START.rst > docs/quickstart.rst
sphinx-build -n -a -b html docs builddocs
#sphinx-build -n -a -b pdf docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..

