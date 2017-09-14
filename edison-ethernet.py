#!/usr/bin/env python

import dbus

s_con = dbus.Dictionary({
    'id': 'resin-wired',
    'type': '802-3-ethernet'})

s_eth = dbus.Dictionary({'assigned-mac-address': 'random'})

con = dbus.Dictionary({
    'connection': s_con,
    'ethernet': s_eth})

print("Creating connection: {}".format(s_con['id']))

bus = dbus.SystemBus()
proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Settings")
settings = dbus.Interface(proxy, "org.freedesktop.NetworkManager.Settings")

settings.AddConnection(con)
print("Connection created, reboot device to take effect.")
