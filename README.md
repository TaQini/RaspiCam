# RaspiCam System
 - take photos by camera of raspi-zero-w 
 - stroage photos to SD card
 - show photos in website

# requirement
 - python3, pip3, Django
 - raspistill
 - hostapd, dnsmasq
 - git, zsh
 - zip

# install 
```
$ sudo apt-get -y install hostapd dnsmasq python3 python3-pip git zsh
$ sudo pip3 install Django
```

# install oh-my-zsh (best shell!)
```
$ sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
```

# configure
 - ap: see doc/ref-Zero-W-AP.md
 - autorun: add start.sh to /etc/rc.local
 - install zsh
 - dns config: see doc/dns-config.md

# sources
 - /etc/apt/sources.list
```shell
 deb http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi
```

# Todo
 - Image operation 
 - ...

