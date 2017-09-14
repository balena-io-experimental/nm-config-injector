apt-get update
apt-get install python python-dbus wget
wget https://raw.githubusercontent.com/resin-io-playground/nm-config-injector/master/edison-ethernet.py -O /tmp/edison-ethernet.py
DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket python /tmp/edison-ethernet.py
