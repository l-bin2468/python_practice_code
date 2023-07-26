#!/usr/bin/env expect

set timeout 5

spawn ssh mrswhite@192.168.37.9

expect "*password:"

send "test20221007\r"

expect "*#"

spawn telnet aixserver
expect "login:"
send "mynamer"
expect "Password:"
send "mypassr"
send "lsr"
send "prtconfr"
expect eof

interact

