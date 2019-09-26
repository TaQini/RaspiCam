# Raspberry Pi Zero W配置Wi-Fi AP

最近在配置Raspberry Pi Zero W,使用的系统为2018-06-27-raspbian-stretch-lite，我们的需求是把这台Raspberry Pi Zero W配置为开放Wi-Fi模式的AP。

Raspberry Pi Zero W只有一块无线网卡，如果被配置成AP模式不是太好操作，可以通过预留的Macro USB接口外接一个USB有线网卡来实现远程访问，当然也可以直接接入显示器，USB Hub外接鼠标键盘操作。

执行如下脚本配置：

```shell
#目前测试发现udhcpd在标准树莓派上能正常工作，但是在Pi Zero W上，重启之后，
#不能正常分配IP，应该是服务在无线网卡没有初始化完成就已经启动导致的，
#我们使用dnsmasq替代后可以正常工作

$ sudo apt-get -y remove udhcpd

$ sudo apt-get -y install hostapd dnsmasq

#备份配置文件
$ sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.bak

#配置分配的IP段
$ sudo sed -i "s/^#dhcp-range=192.168.0.50,192.168.0.150,12h/dhcp-range=192.168.0.50,192.168.0.150,12h/g" /etc/dnsmasq.conf

#AP名字
$ export AP_NAME="AP"

#为无线网卡配置静态IP
$ export WLAN_IP=192.168.0.1

$ sudo ifconfig wlan0 $WLAN_IP

$ sudo sed -i '$a\interface wlan0' /etc/dhcpcd.conf

$ echo "static ip_address=${WLAN_IP}/24" | sudo tee -a /etc/dhcpcd.conf

#hostapd配置，配置为开放模式
$ sudo touch /etc/hostapd/hostapd.conf

$ echo "interface=wlan0" | sudo tee -a /etc/hostapd/hostapd.conf

$ echo "ssid=${AP_NAME}" | sudo tee -a /etc/hostapd/hostapd.conf

#WiFi工作的频段 1-13
$ echo "channel=9" | sudo tee -a /etc/hostapd/hostapd.conf

#硬件工作模式 g simply means 2.4GHz
$ echo "hw_mode=g" | sudo tee -a /etc/hostapd/hostapd.conf

#验证方式为开放模式 1=wpa, 2=wep, 3=both
$ echo "auth_algs=1" | sudo tee -a /etc/hostapd/hostapd.conf
    
# 802.11n support	 	 
$ echo "ieee80211n=1" | sudo tee -a /etc/hostapd/hostapd.conf

#备份配置文件
$ sudo cp /etc/default/hostapd /etc/default/hostapd.bak

#修改配置文件
$ sudo sed -i "s/#DAEMON_CONF=\"\"/DAEMON_CONF=\"\/etc\/hostapd\/hostapd.conf\"/g" /etc/default/hostapd

#启动networking和hostapd服务，注意先后顺序，先使用networking服务设置IP,再更新hostapd
$ sudo service networking restart

$ sudo service hostapd restart

$ sudo service dnsmasq restart

#设置开机启动
$ sudo update-rc.d hostapd enable

#重启设备，检查配置是否已经生效
$ sudo reboot
```

url: http://www.mobibrw.com/2018/13975/comment-page-1?unapproved=3553&moderation-hash=99a64ca085fdb15e1b9a83b18291feb5#comment-3553

