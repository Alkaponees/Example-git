#!/bin/bash
sudo apt update 
sudo apt install -y git
sudo git clone https://github.com/Alkaponees/ICTA-Explorer.git
sudo cd ICTA-Explorer/ 
sudo python -m venv ICTA-env
sudo cd ICTA-env/Scripts
sudo ./activate
sudo pip install aiogram
sudo pip install telegram.ext
sudo pip install pythonBotAPI 