#!/bin/bash

mkdir mysqlworkbench
cd mysqlworkbench
wget http://mirror.f4st.host/archlinux/community/os/x86_64/mysql-workbench-6.3.9-4-x86_64.pkg.tar.xz
sudo pacman -U mysql-workbench-6.3.9-4-x86_64.pkg.tar.xz
cd ..