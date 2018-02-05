from django.db import models
from django.db.models import F, Q

from datetime import datetime, timedelta
from django.utils import timezone

from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType

from htps.models import Building
from .tasks import task_print_zpl

def print_label(printer_slug, doc_type_slug, context_dict=None, **kwargs):
	printer_item = Printer.objects.get(slug=printer_slug)
	doc_item = Document_Template.objects.get(slug=doc_type_slug)

	tcp_ip = printer_item.ip_address
	tcp_port = printer_item.port

	from django.template import Context, Template
	template = Template(doc_item.zpl)
	context = Context(context_dict)
	zpl_string = template.render(context)

	task_print_zpl.delay(tcp_ip,tcp_port,zpl_string)

class Document_Template(models.Model):
	name = models.CharField(max_length=250)
	slug = models.CharField(max_length=128,null=True,blank=True)
	zpl = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return u'%s' % (self.name)

	class Meta:
		verbose_name_plural = "document templates"
		ordering = ['name']

class Printer(models.Model):
	name = models.CharField(max_length=250)
	slug = models.CharField(max_length=128,null=True,blank=True)
	ip_address = models.CharField(max_length=15)
	port = models.IntegerField()
	mac_address = models.CharField(max_length=20)
	enabled = models.BooleanField(default=True)

	def __unicode__(self):
		return u'%s' % (self.name)

	class Meta:
		verbose_name_plural = "printers"
		ordering = ['name']