from django.db import models
from django.utils import timezone
from item.models import Item


class Barrow(models.Model):
	class Meta:
		verbose_name = 'Barrow'
		verbose_name_plural = 'Barrows'
		ordering = (['brw_dt'])

	brw_pk = models.AutoField(verbose_name='Barrow ID', primary_key=True,)
	brw_itm = models.ManyToManyField(Item, verbose_name='Barrow Item')
	brw_ttl = models.DecimalField(verbose_name='Barrow Total', max_digits=6, decimal_places=2)
	brw_dt = models.DateTimeField(verbose_name='Barrow Date', default=timezone.now)

	def __str__(self):
		return self.brw_pk
