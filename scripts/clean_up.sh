#cd ..
find . -name "*.pyc" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
#cd scripts