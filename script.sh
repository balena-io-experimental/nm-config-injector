# Run these commands first, assuming you are using a Debian user image
apt-get update
apt-get install python python-dbus wget
wget https://raw.githubusercontent.com/resin-io-playground/nm-config-injector/master/static-mac.py -O /tmp/static-mac.py

# Generate a MAC address in the form of `AA:BB:CC:DD:EE:FF`, a new one for each device you
# want to use static addresses with. For exmaple using
# https://www.hellion.org.uk/cgi-bin/randmac.pl?scope=local&type=unicast
# Add that address as a command line option to the next line (upper/lowercase does not matter)
DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket python /tmp/static-mac.py
