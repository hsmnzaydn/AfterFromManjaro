#!/bin/bash

mkdir android-studio
cd android-studio
wget https://dl.google.com/dl/android/studio/ide-zips/2.3.2.0/android-studio-ide-162.3934792-linux.zip
unzip android-studio-ide-162.3934792-linux.zip
sudo chown -R root:root android-studio
sudo mv android-studio /opt

LC_ALL=C sh /opt/android-studio/bin/studio.sh
cd ~/$ANDROID_HOME/Android/Sdk/emulator/lib64/libstdc++
mv libstdc++.so.6 libstdc++.so.6.bak
cd ..