#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/numix-circle-icon-theme-git.tar.gz
tar -xvzf numix-circle-icon-theme-git.tar.gz
cd numix-circle-icon-theme-git
makepkg -s 
sudo pacman -U numix-circle-icon-theme-git-0.r16.5a11140-1-any.pkg.tar.xz
cd ..