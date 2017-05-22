#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/google-chrome.tar.gz
tar -xvzf google-chrome.tar.gz
cd google-chrome
makepkg -S
sudo pacman -U google-chrome-58.0.3029.110-1-x86_64.pkg.tar.xz
cd ..

