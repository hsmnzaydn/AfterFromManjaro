#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/phpstorm.tar.gz
tar -xzvf phpstorm.tar.gz
cd phpstorm
makepkg -s
sudo pacman -U phpstorm-2017.1.4-1-x86_64.pkg.tar.xz
cd ..