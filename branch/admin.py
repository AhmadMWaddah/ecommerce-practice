from django.contrib import admin
from branch.models import Branch


class BranchAdmin(admin.ModelAdmin):
	list_display = ('brnch_pk', 'brnch_nme', 'brnch_cntry', 'brnch_eml', 'brnch_www')
	list_display_links = ('brnch_nme', 'brnch_www')
	list_filter = ('brnch_cntry', 'brnch_stt', 'brnch_cty')
	search_fields = ('brnch_nme', 'brnch_cntry', 'brnch_eml', 'brnch_www')
	list_per_page = 25


admin.site.register(Branch, BranchAdmin)
