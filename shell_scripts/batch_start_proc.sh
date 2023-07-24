#!/usr/bin/env bash

proc_grafa="grafana"
proc_isrun=`ps -ef|grep ${proc_grafa}|grep -v grep|wc -l`
if [ ${proc_isrun} == 0 ];then
  eval "systemctl start grafana-server"
  echo "${proc_grafa} start successful."
else
  echo "${proc_grafa} is running."
fi

function proc_isstart() {
  #获取参数
  proc_name=${1}
  proc_isrun=`ps -ef|grep ${proc_name}|grep -v grep|wc -l`

  if [ ${proc_isrun} == 0 ];then
    proc_path=`find /usr1/software -name ${proc_name}-*|awk "NR==1"`
    echo "cd ${proc_path}"
    eval "cd ${proc_path}"
    eval "nohup ./${proc_name} &"
    echo "${proc_name} start successful."
  else
    echo "${proc_name} is running."
  fi
}

proc_isstart "prometheus"
proc_isstart "node_exporter"
proc_isstart "pushgateway"
