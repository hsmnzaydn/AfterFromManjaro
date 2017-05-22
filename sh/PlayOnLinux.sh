#!/bin/bash

mkdir playonlinux
wget http://mirror.f4st.host/archlinux/community/os/i686/playonlinux-4.2.10-1-any.pkg.tar.xz
sudo pacman -U playonlinux-4.2.10-1-any.pkg.tar.xz
cd ..