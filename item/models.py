from django.db import models


def item_image_path(self):
	return f'items/{self.itm_ctgry}/{self.itm_nme}_{self.itm_sku}'


def default_item_image():
	return 'default/default_item_image.png'


class Item(models.Model):
	class Meta:
		verbose_name = 'Item'
		verbose_name_plural = 'Items'
		ordering = (['itm_sku'])

	itm_pk = models.AutoField(verbose_name='Item ID', primary_key=True)
	itm_sku = models.CharField(verbose_name='Item SKU', max_length=20, blank=False, null=False)
	itm_brcd = models.CharField(verbose_name='Item BarCode', max_length=20, blank=False, null=False)
	itm_nme = models.CharField(verbose_name='Item Name', max_length=100, blank=False, null=False)
	itm_desc = models.TextField(verbose_name='Item Description', max_length=3000, blank=False, null=False)
	itm_prc = models.DecimalField(verbose_name='Item Price', max_digits=6, decimal_places=2, default='0.00', blank=False, null=False)
	itm_ctgry = models.ForeignKey('Category', verbose_name='Item Category', on_delete=models.SET_DEFAULT, default='None', blank=False, null=True)
	itm_img = models.ImageField(verbose_name='Item Image', blank=True, null=True, upload_to=item_image_path, default=default_item_image)

	def __str__(self):
		return f'{self.itm_nme}_{self.itm_sku} - {self.itm_ctgry}'


class Category(models.Model):
	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = (['ctgry_nme'])

	ctgry_pk = models.AutoField(verbose_name='Category ID', primary_key=True)
	ctgry_nme = models.CharField(verbose_name='Category Name', max_length=100, blank=False, null=False)
	ctgry_desc = models.TextField(verbose_name='Category Description', max_length=1500, blank=False, null=False)
	ctgry_img = models.ImageField(verbose_name='Category Image', upload_to='category/', blank=True, null=True)

	def __str__(self):
		return self.ctgry_nme
