#!/bin/bash

mkdir monodevelop
cd monodevelop
wget http://mirror.f4st.host/archlinux/extra/os/x86_64/mono-5.0.0.100-1-x86_64.pkg.tar.xz
sudo pacman -U mono-5.0.0.100-1-x86_64.pkg.tar.xz
cd ..