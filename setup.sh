#!/bin/bash
#initial setup
# install dependencies

sudo apt-get update

sudo apt-get install mininet -y

sudo apt-get install apache2 -y  

sudo apt-get install x264 -y

sudo apt-get install gpac -y

sudo apt-get install git -y 

sudo apt-get install npm -y

sudo apt-get install xterm -y

sudo apt install openssh-server -y


sudo npm install -g combine-mpd


git clone https://github.com/rjharris01/comp3004.git

cd comp3004

sudo mv dashjs /var/www/html 

#1200kbps 
sudo x264 --output bbb_1200k.264 --fps 30 --bitrate 1200 --video-filter resize:width=1280,height=720 bbb1.mp4
sudo MP4Box -add bbb_1200k.264 -fps 30 bbb_1200k.mp4
sudo MP4Box -dash 4000 -frag 4000 -rap -segment-name segment_1200k_ bbb_1200k.mp4

#600kbps 
sudo x264 --output bbb_600k.264 --fps 30 --bitrate 600 --video-filter resize:width=1280,height=720 bbb1.mp4
sudo MP4Box -add bbb_600k.264 -fps 30 bbb_600k.mp4
sudo MP4Box -dash 4000 -frag 4000 -rap -segment-name segment_600k_ bbb_600k.mp4


#300kbps 
sudo x264 --output bbb_300k.264 --fps 30 --bitrate 300 --video-filter resize:width=1280,height=720 bbb1.mp4
sudo MP4Box -add bbb_300k.264 -fps 30 bbb_300k.mp4
sudo MP4Box -dash 4000 -frag 4000 -rap -segment-name segment_300k_ bbb_300k.mp4

sudo cp bbb_300k_dash.mpd bbb_dash.mpd

combine-mpd bbb_1200k_dash.mpd bbb_600k_dash.mpd bbb_300k_dash.mpd bbb_combined.mpd

mkdir video

mv segment* video 

mv bbb_* video 

sudo mv video /var/www/html



###

sudo -u test firefox



http://192.168.0.223/video/bbb_combined.mpd