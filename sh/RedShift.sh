#!/bin/bash

mkdir redshift
cd redshift
wget http://mirror.f4st.host/archlinux/community/os/x86_64/redshift-1.11-4-x86_64.pkg.tar.xz
sudo pacman -U redshift-1.11-4-x86_64.pkg.tar.xz
cd ..