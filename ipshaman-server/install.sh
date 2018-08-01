#!/usr/bin/env bash

# ipshaman-server install script
# tested with debian 9.5

if [ "$EUID" -ne 0 ]
    then echo "The script must be run as root."
    exit
fi

# download GeoIP database
mkdir -p /usr/local/share/GeoIP
pushd /usr/local/share/GeoIP
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip GeoLiteCity.dat.gz
popd

# install needed debian packages
apt-get libgeoip-dev python3-pip libcap2-bin

# install needed python packages
pip3 install -r requirements.txt

# copy ipshaman-server code into /opt
mkdir /opt
cp -r ipshaman-server/ /opt

# allow non-root to bind port 80
setcap 'cap_net_bind_service=+ep' /usr/bin/python3.5

# create systemd service file
cp ipshaman.service /lib/systemd/system/

# create ipshaman user
useradd -m -s /sbin/nologin -d /opt/ipshaman-server ipshaman
chown ipshaman:ipshaman -R /opt/ipshaman-server

# set ipshaman to start on boot & start ipshaman
systemctl enable ipshaman
systemctl start ipshaman
