# django-zebraprinters
Print ZPL to Zebra Printers

**Requires Celery !!**
I am planning to make this a setting.

## How To Use
```
from zebraprinters import models as zebraprinters

context_dict = {
	'property': 'value',
}

zebraprinters.print_label('printer_slug','doc_slug',context_dict)
```

## Wishlist
- Allow non-celery print jobs with a settings variable