#!/bin/bash

mkdir intellijidea
cd intellijidea
wget http://mirror.f4st.host/archlinux/community/os/i686/intellij-idea-community-edition-2:2017.1.2-1-any.pkg.tar.xz
sudo pacman -U intellij-idea-community-edition-2_2017.1.2-1-any.pkg.tar.xz.part
cd ..
