Install:

git: https://github.com/irinarozalio/mon_prom_grafana_project

cd mon_prom_grafana_project


Run docker-compose with following 3 parameters: 

· Prometheus version

· Prometheus Retention in hours 

· Grafana version:


python monitor_prom_graf.py -h

Monitoring Prometheus-Grafana...

usage: monitor_prom_graf.py [-h] --prometheus_version PROMETHEUS_VERSION
                            --prometheus_ret_hour PROMETHEUS_RET_HOUR
                            --grafana_version GRAFANA_VERSION

Example:

For prometheus version 1.x.x:

python monitor_prom_graf.py --prometheus_version v1.2.1 --prometheus_ret_hour 200h --grafana_version 6.1.3

For prometheus version 2.x.x:

python monitor_prom_graf.py --prometheus_version v2.9.2 --prometheus_ret_hour 200h --grafana_version 6.1.6

Prerequisites:

Docker Engine >= 1.13

Docker Compose >= 1.11

Containers:

· Prometheus --> http://<host-ip>:9090

· Grafana --> http://<host-ip>:3000


CONTAINER ID        IMAGE                    COMMAND                  CREATED             STATUS              PORTS                    NAMES

5a885925432d        prom/prometheus:v1.2.1   "/bin/prometheus --c…"   19 seconds ago      Up 17 seconds       0.0.0.0:9090->9090/tcp   prometheus

8df96f8fde36        grafana/grafana:6.1.3    "/setup.sh"              19 seconds ago      Up 17 seconds       0.0.0.0:3000->3000/tcp   grafana



The Monitor Services Dashboard shows the following metrics:

· Prometheus container uptime, monitoring stack total memory usage

· Prometheus local storage memory chunks and series 

· Container CPU usage graph 

· Container memory usage graph 

· Prometheus chunks to persist and persistence urgency graphs 

· Prometheus chunks ops and checkpoint duration graphs 

· Prometheus samples ingested rate, target scrapes and scrape duration graphs 

· Prometheus HTTP requests graph 

· Prometheus alerts graph