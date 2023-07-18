#!/usr/bash

# 用户数组
arr_user = ("root", "user")

# 所属用户组
arr_group = "root"

# 循环数组
for((i=0;i<${#arr_user[*]};i++))
do
  # 添加用户
  eval "sudo useradd -d /usr1/${arr_user[i]} -g ${arr_group} ${arr_user[i]}"

  # 修改密码   命令1
  # echo 123456|passwd --stdin ${arr_user[i]}
  # 修改密码   命令2
  echo "${arr_user[i]}:123456"|chpasswd

  # 添加用户至 sudoers 文件，使用 sudo 运行该脚本，>> 为追加重定向
  echo "${arr_user[$i]}    ALL=(ALL)       ALL" >> /etc/sudoers
done

