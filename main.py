#!/usr/python env
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Ewerton Oliveira (TcCMBr)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import ssh
import collections
import json
import re


class Main:

    def __init__(self):
        self.ssh = ssh.Ssh()

        host = self.host()

        for h in host:
            comentario = re.compile('[#]+')

            if len(h[0]) > 1 and not comentario.search(h[0]):
                try:
                    ip = h[0]
                    username = h[1]
                    password = h[2]

                    if 3 == len(h):
                        port = 22
                    else:
                        port = int(h[3])

                    print
                    print 'Conectando em %s na porta %s' % (ip, port)
                    if self.ssh.connect(host=ip, usuario=username, senha=password, porta=port) is True:
                        self.clone_mac_detect()
                except Exception as e:
                    print 'Não foi possível conectar. Algo errado com as informações para conexão.'

    @staticmethod
    def host():
        f = open('hosts.txt', 'r')
        painel = []

        for l in f.readlines():
            painel.append(l.split(' '))

        f.close()

        return painel

    def clone_mac_detect(self):
        stdin, stdout, stder = self.ssh.run('wstalist')

        if not stder.read():
            f = open('stalist.json', 'w')
            f.write(stdout.read())
            f.close()

            with open('stalist.json') as stalist:
                filejson = json.load(stalist)

            mac_list = []
            for i in filejson:
                mac_list.append(i['mac'])

            duplicados = [item for item, count in collections.Counter(mac_list).items() if count > 1]

            print
            if duplicados:
                for mac in duplicados:
                    print 'MAC %s duplicado' % mac
            else:
                print 'Nenhum MAC duplicado. =)'

            self.ssh.run('exit;')

if __name__ == "__main__":
    Main()
