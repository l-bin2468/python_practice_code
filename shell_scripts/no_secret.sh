#!/usr/bin/env bash

host=
user=
password=
match_str=

expect <<ENF
#�������
set timeout 5

#��������ʼ������������ָ������
spawn ssh ${user}@${host}

#��ȡƥ����Ϣƥ��ɹ���ִ��expect����ĳ�����
#��������̷����ַ���
expect "login:" {send "${user}"}
expect "Password:" {send "${password}"}
expect "${match_str}" {send "ls -l"}

expect eof
##�����û�������Ȩ�޽�������̨
#interact
ENF

pwd