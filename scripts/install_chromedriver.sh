#!/usr/bin/env bash
rm chromedriver_linux64.zip
wget -N https://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv -f chromedriver /usr/local/share/chromedriver
sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver -f
sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver -f
