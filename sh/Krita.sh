#!/bin/bash

mkdir krita
cd krita
wget http://mirror.f4st.host/archlinux/staging/os/x86_64/krita-3.1.3-2-x86_64.pkg.tar.xz
sudo pacman -U krita-3.1.3-2-x86_64.pkg.tar.xz
cd ..
