#!/usr/bin/bash

instance_name=`hostname -f|cut -d'.' -f1`   #截取主机名

if [ ${instance_name} == "localhost" ];then
  echo "Must FQDN hostname"   #要求主机名不能是localhost，不要主机名区别不了
  exit 1
fi

#定义key
label_wait="count_netstat_wait_connections"
#定义value
count_netstat_wait_connections=`netstat -an|grep -i wait|wc -l`

echo "${label_wait}:${count_netstat_wait_connections}"

#推送数据给pushgateway
echo "${label_wait} ${count_netstat_wait_connections}"|curl --data-binary @- http://192.168.3.35:9091/metrics/job/pushgateway/instance/${instance_name}


#定义key
label_wait="count_coredump"
#定义value
count_coredump=`ls -lrt /var/lib/systemd/coredump|grep "^-"|wc -l`

echo "${label_wait}:${count_coredump}"

#推送数据给pushgateway
echo "${label_wait} ${count_coredump}"|curl --data-binary @- http://192.168.3.35:9091/metrics/job/pushgateway/instance/${instance_name}

