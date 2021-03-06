#!/bin/bash

# The default update from python 2 to python 3 

#Step 1:- Install ppa

sudo add-apt-repository -y  ppa:deadsnakes/ppa


#Step 2:- Update packeges

sudo apt-get update -qq


#Step 3:- Upgrade python 2.x to python 3.x

sudo apt-get install -yy python3.6 
sudo apt-get install -yy python3.7 

#PiP installation
sudo apt install -yy python3-pip 
#Set priority
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1 
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2 

#installation done

echo "##### Current python Version ######"
sudo python3 --version

echo "#############################################################"

echo "All done!"
