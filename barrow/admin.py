from django.contrib import admin
from barrow.models import Barrow


class BarrowAdmin(admin.ModelAdmin):
	list_display = ('brw_pk', 'brw_dt', 'brw_ttl')
	list_display_links = ('brw_pk',)
	list_filter = ('brw_itm',)
	search_fields = ('brw_itm',)
	list_per_page = 25


admin.site.register(Barrow, BarrowAdmin)
