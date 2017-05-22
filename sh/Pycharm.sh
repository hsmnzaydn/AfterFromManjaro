#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/pycharm-community.tar.gz
tar -xvzf pycharm-community.tar.gz
cd pycharm-community
makepkg -s
sudo pacman -U pycharm-community-2017.1.2-1-any.pkg.tar.xz
cd ..