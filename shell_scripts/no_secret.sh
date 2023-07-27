#!/usr/bin/env bash

host=
user=
password=
match_str=

expect <<ENF
#定义变量
set timeout 5

#交互程序开始后面跟命令或者指定程序
spawn ssh ${user}@${host}

#获取匹配信息匹配成功则执行expect后面的程序动作
#用于向进程发送字符串
expect "login:" {send "${user}"}
expect "Password:" {send "${password}"}
expect "${match_str}" {send "ls -l"}

expect eof
##允许用户交互，权限交给控制台
#interact
ENF

pwd