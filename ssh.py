#!/usr/bin/env python
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

import paramiko
import re


class Validacao:

    def __init__(self):
        pass

    @staticmethod
    def valida_usuario(i, P, S, W):
        if len(P) <= 0:
            return False

        return True

    @staticmethod
    def valida_senha(i, P, S, W):
        if len(P) <= 0:
            return False

        return True

    @staticmethod
    def valida_ip(i, P, S, W):
        valid = re.compile('[\d.]+')
        valid = valid.match(S)

        if valid is None or len(P) == 16:
            return False

        return True


class Ssh(Validacao):

    conexao = None
    host = ''
    username = ''
    password = ''
    port = 0

    def connect(self, host, usuario, senha, porta):
        self.host = host
        self.username = usuario
        self.password = senha
        self.port = int(porta)

        try:
            self.conexao = paramiko.SSHClient()
            self.conexao.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.conexao.connect(host, username=usuario, password=senha, port=porta)
            self.save_key_server()

        except paramiko.BadHostKeyException:
            print 'Chave de Host ruim.'
            return False
        except paramiko.AuthenticationException:
            print 'Falha na autenticação.'
            return False
        except paramiko.SSHException:
            print 'Não foi possível ter acesso.'
            return False
        except Exception:
            print 'Não foi possível conectar.'
            return False
        else:
            return True

    def run(self, command):
        return self.conexao.exec_command(command)

    def open_session(self):
        self.channel = self.get_transport().open_session()

    def get_transport(self):
        return self.conexao.get_transport()

    def is_active(self):
        return self.get_transport().is_active()

    def is_authenticated(self):
        return self.get_transport().is_authenticated()

    def open_sftp(self, host, port, username, password):
        t = paramiko.Transport((host, port))
        t.connect(username, password)
        sftp = paramiko.SFTPClient.from_transport(t)

        return sftp

    def save_key_server(self):
        try:
            key = self.get_transport().get_remote_server_key()
            self.conexao.save_host_keys('~/.ssh/know_hosts')
        except IOError:
            print 'Não foi possivel salvar a host key do servidor!'

    def cancel_execution(self):
        self.run('^C')
