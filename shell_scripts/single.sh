#!/usr/bash

# �û�����
arr_user = ("root", "user")

# �����û���
arr_group = "root"

# ѭ������
for((i=0;i<${#arr_user[*]};i++))
do
  # ����û�
  eval "sudo useradd -d /usr1/${arr_user[i]} -g ${arr_group} ${arr_user[i]}"

  # �޸�����   ����1
  # echo 123456|passwd --stdin ${arr_user[i]}
  # �޸�����   ����2
  echo "${arr_user[i]}:123456"|chpasswd

  # ����û��� sudoers �ļ���ʹ�� sudo ���иýű���>> Ϊ׷���ض���
  echo "${arr_user[$i]}    ALL=(ALL)       ALL" >> /etc/sudoers
done

