#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/netbeans-javase.tar.gz
tar -xvzf netbeans-javase.tar.gz
cd netbeans-javase
makepkg -s
sudo pacman -U netbeans-javase-8.2-1-any.pkg.tar.xz
cd ..