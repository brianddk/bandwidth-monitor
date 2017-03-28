#!/bin/bash
srvcname=bandwidth-monitor.service
srvcpath=/lib/systemd/system
systemctl stop $srvcname 1> /dev/null 2> /dev/null
fqdnname="$(hostname --short).$(grep domain /etc/resolv.conf | awk '{print $2}')"
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root.  Run this script with sudo" 1>&2
   echo "    'sudo $0'" 1>&2
   exit 1
fi
sed -e "s/hostname/$fqdnname/" $srvcname > $srvcpath/$srvcname
chmod 644 $srvcpath/$srvcname
systemctl daemon-reload
systemctl enable $srvcname
systemctl start $srvcname
tail /var/log/syslog
