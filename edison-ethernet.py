#!/usr/bin/env python

import dbus

s_con = dbus.Dictionary({
    'id': 'resin-wired',
    'type': 'ethernet'})

s_con_smsc95 = dbus.Dictionary({
    'ethernet.cloned-mac-address': 'stable',
    'match-device': 'driver:smsc95xx'})

s_ip4 = dbus.Dictionary({'method': 'auto'})

s_ip6 = dbus.Dictionary({
    'addr-gen-mode':'stable-privacy',
    'method': 'auto'})

con = dbus.Dictionary({
    'connection': s_con,
    'connection-smsc9514': s_con_smsc95,
    'ipv4': s_ip4,
    'ipv6': s_ip6})

print("Creating connection: {}".format(s_con['id']))

bus = dbus.SystemBus()
proxy = bus.get_object("org.freedesktop.NetworkManager", "/org/freedesktop/NetworkManager/Settings")
settings = dbus.Interface(proxy, "org.freedesktop.NetworkManager.Settings")

settings.AddConnection(con)
print("Connection created, reboot device to take effect.")
