import argparse
import os
import time
import datetime
import logging
import sys
from pprint import pprint
import argparse
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


def setup_logger(logger_name, log_file, level=logging.INFO):
	l = logging.getLogger(logger_name)
	formatter = logging.Formatter('%(asctime)s : %(message)s')
	fileHandler = logging.FileHandler(log_file, mode='w')
	fileHandler.setFormatter(formatter)
	streamHandler = logging.StreamHandler()
	streamHandler.setFormatter(formatter)
	l.setLevel(level)
	l.addHandler(fileHandler)
	l.addHandler(streamHandler)


def send_mail(send_from, send_to, subject, text, files=None, server="****"):
	assert isinstance(send_to, list)
	msg = MIMEMultipart()
	msg['From'] = send_from
	msg['To'] = COMMASPACE.join(send_to)
	msg['Date'] = formatdate(localtime=True)
	msg['Subject'] = subject
	msg.attach(MIMEText(text))
	smtp = smtplib.SMTP(server)
	smtp.sendmail(send_from, send_to, msg.as_string())
	smtp.close()

def parse_args():
	parser = argparse.ArgumentParser(description='PROMETHEUS_VERSION,PROMETHEUS_RET_HOUR,GRAFANA_VERSION')
	parser.add_argument('--prometheus_version', default="v2.9.2", required=True)
	parser.add_argument('--prometheus_ret_hour', default="200h", required=True)
	parser.add_argument('--grafana_version', default="6.1.3", required=True)
	return parser.parse_args()

def main():
	print('Monitoring Prometheus-Grafana...')
	ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
	args = parse_args()
	pprint ("The Prometheus version is " + args.prometheus_version)
	pprint ("The Prometheus Retention in hours is " + args.prometheus_ret_hour)
	pprint ("The Grafana version is " + args.grafana_version)
	start_time = time.time()
	# setup_logger('log','/home/ira/mon_prom_grafana_project/logs/prom_graf.txt')
	# log = logging.getLogger('log')
	# log.info('Monit_Prom_Graf:')

	prom_ver = "v1."
	args.prometheus_version.startswith(prom_ver)

	if (args.prometheus_version.startswith(prom_ver)):
		print("The Prometheus version is 1.x.x (" + args.prometheus_version + ")")
		docker_comp_comm = "ADMIN_USER=admin ADMIN_PASSWORD=admin PROMETHEUS_VERSION={0} PROMETHEUS_RET_HOUR={1} GRAFANA_VERSION={2} docker-compose -f docker-compose.yml up -d".format(args.prometheus_version,args.prometheus_ret_hour,args.grafana_version)
	else:
		print("The Prometheus version is 2.x.x (" + args.prometheus_version + ")")
		docker_comp_comm = "ADMIN_USER=admin ADMIN_PASSWORD=admin PROMETHEUS_VERSION={0} PROMETHEUS_RET_HOUR={1} GRAFANA_VERSION={2} docker-compose -f docker-compose_2.yml up -d".format(args.prometheus_version,args.prometheus_ret_hour,args.grafana_version)
	
	pprint (docker_comp_comm)
	os.system(docker_comp_comm)
	elapsed_time = time.time() - start_time
	pprint ("Elapsed time: " + "%02d:%02d" % divmod(elapsed_time, 60))


if __name__ == "__main__":
	main()  





