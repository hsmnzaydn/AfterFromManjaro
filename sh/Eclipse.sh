#!/bin/bash

mkdir eclipse
cd eclipse
wget http://mirror.f4st.host/archlinux/extra/os/x86_64/eclipse-java-4.6.3-1-x86_64.pkg.tar.xz
sudo pacman -U eclipse-java-4.6.3-1-x86_64.pkg.tar.xz
cd ..
