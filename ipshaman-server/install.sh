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
wget https://dl.miyuru.lk/geoip/maxmind/city/maxmind.dat.gz
gunzip GeoLiteCity.dat.gz
mv maxmind.dat GeoLiteCity.dat
popd

# install needed debian packages
apt-get libgeoip-dev libcap2-bin python3.8 python3.8-dev

# install needed python packages
python3.8 -m pip install -r requirements.txt

# change index to use proper full path
sed -i -e 's/index.html/\/opt\/ipshaman-server\/index.html/g' ipshaman-server/server.py

# copy ipshaman-server code into /opt
mkdir /opt
cp -r ipshaman-server/ /opt

# allow non-root to bind port 80
setcap 'cap_net_bind_service=+ep' /usr/bin/python3.8

# create systemd service file
cp ipshaman.service /lib/systemd/system/

# create ipshaman user
useradd -m -s /sbin/nologin -d /opt/ipshaman-server ipshaman
chown ipshaman:ipshaman -R /opt/ipshaman-server

# set ipshaman to start on boot & start ipshaman
systemctl enable ipshaman
systemctl start ipshaman
