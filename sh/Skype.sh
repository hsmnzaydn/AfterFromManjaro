#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/skypeforlinux.tar.gz
tar -xvzf skypeforlinux.tar.gz
cd skypeforlinux
makepkg -s
sudo pacman -U skypeforlinux-5.1.0.1-1-x86_64.pkg.tar.xz
cd ..