#!/bin/bash

wget https://aur.archlinux.org/cgit/aur.git/snapshot/nylas-mail-bin.tar.gz
tar -xvzf nylas-mail-bin.tar.gz
cd nylas-mail-bin
makepkg -s
sudo pacman -U nylas-mail-bin-2.0.32-1-x86_64.pkg.tar.xz
cd ..
