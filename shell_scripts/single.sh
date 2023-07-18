#!/usr/bin/bash

#用户数组
arr_user=("user")

# 所属用户组
arr_group="user"

#result=`awk -F: 'NR==1{print $1}' /etc/group|grep ${arr_group}`
result=$(grep "user" /etc/group|awk -F: 'NR==1{print $1}')

#如果用户组不存在
if [ ${result} != $arr_group ]
then
  eval "sudo groupadd ${arr_group}"
#elif [ "${result}" == "$arr_group" ]
#then
#   echo "a 等于 b"
fi

#循环数组
for((i=0;i<${#arr_user[*]};i++))
do
  #添加用户，创建后会带配置文件
  eval "sudo useradd -d /usr1/${arr_user[i]} -g ${arr_group} ${arr_user[i]}"

  #修改密码   命令1
  #echo 123456|passwd --stdin ${arr_user[i]}
  #修改密码   命令2
  echo "${arr_user[i]}:123456"|chpasswd

  #添加用户至 sudoers 文件，使用 sudo 运行该脚本，>> 为追加重定向
  echo "${arr_user[$i]}    ALL=(ALL)       ALL" >> /etc/sudoers
done
