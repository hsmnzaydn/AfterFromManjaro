#!/bin/bash

mkdir anaconda
cd anaconda
wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh
sh Anaconda3-4.3.1-Linux-x86_64.sh
sudo conda update conda
cd ..
