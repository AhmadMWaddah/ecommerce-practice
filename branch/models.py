from django.db import models


def branch_image_path(self):
	return f'branches/{self.brnch_pk} - {self.brnch_nme}/{"branch_image.png"}'


def default_branch_image():
	return 'default/default_branch_image.png'


class Branch(models.Model):
	class Meta:
		verbose_name = 'Branch'
		verbose_name_plural = 'Branches'
		ordering = (['brnch_cntry'])

	brnch_pk = models.AutoField(verbose_name='Branch ID', primary_key=True)
	brnch_nme = models.CharField(verbose_name='Branch Name', max_length=100, blank=False, null=False)
	brnch_cntry = models.CharField(verbose_name='Branch Country', max_length=100, blank=False, null=False)
	brnch_stt = models.CharField(verbose_name='Branch State', max_length=100, blank=False, null=False)
	brnch_cty = models.CharField(verbose_name='Branch City', max_length=100, blank=False, null=False)
	brnch_strt = models.CharField(verbose_name='Branch Street', max_length=150, blank=False, null=False)
	brnch_bx = models.CharField(verbose_name='Branch Box Code', max_length=8, blank=True, null=True, default=None)
	brnch_phn = models.CharField(verbose_name='Branch Phone', max_length=15, blank=True, null=True, default=None, unique=True)
	brnch_fx = models.CharField(verbose_name='Branch Fax', max_length=15, blank=True, null=True, default=None, unique=True)
	brnch_mbl = models.CharField(verbose_name='Branch Mobile', max_length=15, blank=True, null=True, default=None, unique=True)
	brnch_eml = models.EmailField(verbose_name='Branch Email', blank=False, null=False)
	brnch_www = models.URLField(verbose_name='Branch Website', max_length=150, blank=False, null=False)
	brnch_loc = models.CharField(verbose_name='Branch Location', max_length=600, blank=False, null=False)
	brnch_img = models.ImageField(verbose_name='Branch Image', blank=True, null=True, upload_to=branch_image_path, default=default_branch_image)

	def __str__(self):
		return self.brnch_nme
