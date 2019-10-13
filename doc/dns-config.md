## add follow code to /etc/dnsmasq.conf
```
resolv-file=/etc/pi_dns.conf
strict-order
cache-size=1500
listen-address=127.0.0.1,192.168.0.1
address=/www.raspicam.com/192.168.0.1
```

## create new file by ` $ sudo vim /etc/pi_dns.conf` 
```
nameserver 127.0.0.1
```


