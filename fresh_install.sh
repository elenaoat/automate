#!/bin/sh
apt-get update  # To get the latest package lists
apt-get install nginx -y
apt-get install python-pip -y
apt-get install git -y
sudo pip install python-twisted
sudo pip install autobahn

