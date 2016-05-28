#!/bin/bash

apt-get update
apt-get install gcc
apt-get install python
apt-get install python-dev
apt-get install build-essential
apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
apt-get install python-setuptools

easy_install pip
pip install --upgrade pip
pip install paramiko --upgrade