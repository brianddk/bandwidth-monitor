#!/bin/bash
srvcname=bandwidth-monitor.service
srvcpath=/lib/systemd/system
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root.  Run this script with sudo" 1>&2
   echo "    'sudo $0'" 1>&2
   exit 1
fi
sed -e "s/hostname/$(hostname --long)/" $srvcname > $srvcpath/$srvcname
chmod 644 $srvcpath/$srvcname
systemctl daemon-reload
systemctl enable $srvcname
systemctl start $srvcname
tail /var/log/syslog
