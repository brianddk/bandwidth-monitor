#!/bin/bash
sudo cp bandwidth-monitor.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/bandwidth-monitor.service
#chmod +x /home/pi/src/bandwidth-monitor/pyWebSrv.py
sudo systemctl daemon-reload
sudo systemctl enable bandwidth-monitor.service
sudo systemctl start bandwidth-monitor.service
