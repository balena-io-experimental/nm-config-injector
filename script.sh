apt-get update
apt-get install python wget build-essential
cd /tmp/
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install dbus-python
wget https://raw.githubusercontent.com/resin-io-playground/nm-config-injector/master/edison-ethernet.py
DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket python edison-ethernet.py
