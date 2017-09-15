#!/usr/bin/env python
"""
This script will use DBus to communicate with the HostOS networkManager
and create a connection setting with a static MAC address, defined by
the command-line option to this script. The resulting file will be like
this (with different uuid and cloned-mac-address fields, naturally):

```
[connection]
id=resin-wired
uuid=11111111-2222-3333-4444-555555555555
type=ethernet
permissions=

[ethernet]
cloned-mac-address=AA:BB:CC:DD:EE:FF
mac-address-blacklist=

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
method=auto
```

"""

import sys
import dbus

if len(sys.argv) < 2:
    print("Need a MAC address as an argument! Please re-run the script with that.")
    sys.exit(1)

MAC = sys.argv[1]
print(MAC)

s_con = dbus.Dictionary({
    'id': 'resin-wired',
    'type': '802-3-ethernet'})

s_eth = dbus.Dictionary({'assigned-mac-address': MAC})

con = dbus.Dictionary({
    'connection': s_con,
    '802-3-ethernet': s_eth})

print("Creating connection: {} with MAC: {}".format(s_con['id'], MAC))

bus = dbus.SystemBus()
proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Settings")
settings = dbus.Interface(proxy, "org.freedesktop.NetworkManager.Settings")

settings.AddConnection(con)
print("Connection created, reboot device to take effect.")
