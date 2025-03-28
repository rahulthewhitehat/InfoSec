#!/bin/bash

# Step 1: Check SELinux Status
sestatus

# Step 2: Enable SELinux (Enforcing Mode)
sudo setenforce 1
sudo sed -i 's/^SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config
sestatus

# Step 3: Create a Test File
sudo touch /root/securefile

# Step 4: Change Security Context of the File
sudo chcon -t httpd_sys_content_t /root/securefile

# Step 5: Start Apache Server (If Installed)
sudo systemctl start httpd

# Step 6: Test Access Control (Apache User Trying to Read File)
sudo runuser -u apache -- cat /root/securefile

# Step 7: Check SELinux Denials (AVC Logs)
sudo ausearch -m AVC,USER_AVC -ts recent

# Step 8: Switch to Permissive Mode
sudo setenforce 0
sudo sed -i 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config
sestatus

# Step 9: Check SELinux Logs Again
sudo ausearch -m AVC,USER_AVC -ts recent

# Step 10: Disable SELinux (If Required, Needs Reboot)
sudo sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/selinux/config'
