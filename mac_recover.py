#!/usr/bin/env python

import subprocess

subprocess.call("sudo ifconfig eth0 hw ether $(ethtool -P eth0 | awk '{print $3}')", shell=True)
