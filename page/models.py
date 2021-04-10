from django.db import models
import datetime


def showcase_image_path(self):
	return f'showcases/{self.shwcs_nme}/{"showcase_image.png"}'


def default_showcase_image():
	return 'default/default_showcase_image.png'


class Showcase(models.Model):
	class Meta:
		verbose_name = 'Showcase'
		verbose_name_plural = 'Showcases'

	shwcs_pk = models.AutoField(verbose_name='Showcase ID', primary_key=True)
	shwcs_nme = models.CharField(verbose_name='Showcase Name', max_length=100, blank=False, null=False)
	shwcs_desc = models.TextField(verbose_name='Showcase Description', max_length=1500, blank=False, null=False)
	shwcs_dte = models.DateTimeField(verbose_name="Showcase Date", default=datetime.datetime.now().time(), blank=False, null=False)
	shwcs_img = models.ImageField(verbose_name='Showcase Image', blank=True, null=True, upload_to=showcase_image_path, default=default_showcase_image)

	def __str__(self):
		return self.shwcs_nme
