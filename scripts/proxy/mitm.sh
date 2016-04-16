#!/bin/bash
./clean.sh
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8080
mitmdump -T --host -s request.py
