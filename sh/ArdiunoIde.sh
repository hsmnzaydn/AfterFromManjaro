#!/bin/bash

mkdir arduino
cd arduino
wget http://mirror.f4st.host/archlinux/community/os/x86_64/arduino-1:1.8.2-1-x86_64.pkg.tar.xz
sudo pacman -U arduino-1_1.8.2-1-x86_64.pkg.tar.xz
cd ..