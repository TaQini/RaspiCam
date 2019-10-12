#!/bin/zsh
/home/pi/RaspiCam/manage.py runserver 0.0.0.0:8080 & 

# add follow code to /etc/rc.local before exit 0
# ...
# /home/pi/RaspiCam/start.sh
# exit 0
