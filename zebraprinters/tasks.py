from __future__ import absolute_import

from celery import shared_task

from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings

import traceback


@shared_task
def task_print_zpl(tcp_ip,tcp_port,zpl_string):
	import socket

	BUFFER_SIZE = 1024

	print "Sending ZPL Print."
	print "IP: %s" % (tcp_ip)
	print "PORT: %s" % (tcp_port)

	# Create a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to printer
	s.connect((tcp_ip, tcp_port))
	print "Connected."

	# Send data
	s.send(bytes(zpl_string))
	print "Sent."

	# Close connection
	s.close()
	print "Closing Connection."