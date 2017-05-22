#!/bin/bash

mkdir atom
cd atom
wget http://mirror.f4st.host/archlinux/community/os/x86_64/atom-1.17.0-1-x86_64.pkg.tar.xz
sudo pacman -U atom-1.17.0-1-x86_64.pkg.tar.xz
cd ..