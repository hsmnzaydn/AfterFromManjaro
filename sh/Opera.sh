#!/bin/bash

mkdir opera
cd opera
wget http://mirror.f4st.host/archlinux/community/os/x86_64/opera-45.0.2552.812-1-x86_64.pkg.tar.xz
sudo pacman -U opera-45.0.2552.812-1-x86_64.pkg.tar.xz
cd ..