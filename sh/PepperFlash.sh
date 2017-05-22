#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/pepper-flash.tar.gz
tar -xzvf pepper-flash.tar.gz
cd pepper-flash
makepkg -s
sudo pacman -U pepper-flash-25.0.0.171-1-x86_64.pkg.tar.xz
cd ..
