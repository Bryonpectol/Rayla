#!/bin/bash

#mkdir /rayla

#mkdir /rayla/python

#mkdir /rayla/reconnassiance

#mkdir /rayla/resource-development

#mkdir /rayla/initial-access

#mkdir /rayla/execution

#mkdir /rayla/persistence

#mkdir /rayla/privilege-escalation

#mkdir /rayla/defense-evasion

#mkdir /rayla/credential-access

#mkdir /rayla/discovery

#mkdir /rayla/lateral-movement

#mkdir /rayla/collection

#mkdir /rayla/command-control

#mkdir /rayla/exfiltration

#mkdir /rayla/impact

#mkdir /rayla/credential-access/access-point-scan-reporst

#mkdir /rayla/credential-access/cracked-wifi-passwords

#mkdir /rayla/credential-access/focused-scan-reports

#mkdir /rayla/credential-access/targeted-access-point

pip install python-nmap

cd /

git clone https://github.com/Bryonpectol/rayla.git

echo "alias rayla='python3 /rayla/python/rayla.py'" > ~/.bashrc
