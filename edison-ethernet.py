#!/usr/bin/env python

import dbus
import sys

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
    'ethernet': s_eth})

print("Creating connection: {} with MAC: {}".format(s_con['id'], MAC))

bus = dbus.SystemBus()
proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Settings")
settings = dbus.Interface(proxy, "org.freedesktop.NetworkManager.Settings")

settings.AddConnection(con)
print("Connection created, reboot device to take effect.")
