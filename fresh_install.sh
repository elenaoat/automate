#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install nginx -y
apt-get install python-pip -y
apt-get install git -y
apt-get install python-dev -y
apt-get install build-essential -y
sudo add-apt-repository ppa:twisted-dev/ppa
sudo pip install twisted
sudo pip install autobahn
####### LATER steps #############

# perform vundle install + install nerdcommenter
#change the mapleader in .vimrc: let mapleader="," for nerdcommenter

#bind '"\C-p": shell-kill-word' #to make Ctrl+p remove a word in front of the cursor
#sudo update-alternatives --config editor # to choose vim as default editor
