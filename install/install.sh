#!/bin/bash

apt-get update
apt-get install gcc
apt-get install python
apt-get install python-dev
apt-get install build-essential
apt-get install apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex \
python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test \
libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev
apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
apt-get install python-setuptools
easy_install pip
easy_install greenlet
easy_install gevent
pip install --upgrade pip
pip install paramiko --upgrade