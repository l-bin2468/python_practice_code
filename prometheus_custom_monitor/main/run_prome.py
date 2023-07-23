# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/7/23 12:37
# Describe: Prometheus monitor server port
import random

import prometheus_client
from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask

from utils.connLinux import ConnLinux

app = Flask(__name__, static_url_path="/main")
# 实例化 REGISTRY
registry = CollectorRegistry(auto_describe=False)
gauge = Gauge(
    name="Server_port",
    documentation="monitor server port status.",
    labelnames=["sertype", "host", "port"],
    registry=registry
)


@app.route("/metrics")
def requests_count():
    result = ConnLinux().exec_command("ls -l /root/shell_scripts|grep '^-'|wc -l")

    # 模拟多个值传入
    rows = [
        {"sertype": "zookeeper", "host": "192.168.1.22", "port": "2181", "status": result},
        {"sertype": "zookeeper", "host": "192.168.1.33", "port": "2181", "status": random.randint(10, 30)},
        {"sertype": "zookeeper", "host": "192.168.1.44", "port": "2181", "status": random.randint(15, 35)},
        {"sertype": "mysql", "host": "192.168.1.88", "port": "3306", "status": random.randint(5, 25)},
        {"sertype": "mysql", "host": "192.168.1.99", "port": "3306", "status": random.randint(20, 40)}
    ]

    for row in rows:
        sertype = "".join(row.get("sertype"))
        ip = "".join(row.get("host"))
        port = "".join(row.get("port"))
        status = row.get("status")
        gauge.labels(sertype, ip, port).set(status)
    return Response(prometheus_client.generate_latest(registry), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=31672, debug=True)
