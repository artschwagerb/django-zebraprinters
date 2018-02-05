from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import ugettext_noop as _

class Command(BaseCommand):
	finish_msg = ''
	args = '(none)'
	help = 'Test zebraprinters'	

	def handle(self, *args, **options):
		from zebraprinters import models as zebraprinters

		context_dict = {
			'property': 'value',
		}

		zebraprinters.print_label('printer_slug','doc_slug',context_dict)