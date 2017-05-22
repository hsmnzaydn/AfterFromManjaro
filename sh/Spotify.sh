#!/bin/bash


sudo -Rsnc spotify
sudo -Syyuu
sudo pacman -Scc
yaourt -S --m-arg --skippgpcheck --noconfirm libopenssl-1.0-compat
yaourt -S --m-arg --skippgpcheck --noconfirm libcurl-openssl-1.0
yaourt -S spotify