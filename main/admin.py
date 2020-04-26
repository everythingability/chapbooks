
from django.contrib import admin
#admin.site.site_header = "MY DJANGO"
#admin.site.site_title = "Admin"
#admin.site.index_title = ""

from django.contrib.contenttypes.admin import  GenericTabularInline
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django.contrib import admin

from .models import *

class PageAdmin(admin.ModelAdmin):
	#fields = ('name', )
	exclude =      ('slug', )
	list_display = ('name', )
	search_fields = ['name', "text"]
admin.site.register(Page, PageAdmin)

class ChapbookAdmin(admin.ModelAdmin):
	#fields = ('name', )
	#exclude =      ('slug', )
	#list_display = ('name', )
	search_fields = ['name', "text"]
admin.site.register(Chapbook, ChapbookAdmin)

class ImageAdmin(admin.ModelAdmin):
	''
	#fields = ('name', )
	#exclude =      ('slug', )
	#list_display = ('name', )
	#search_fields = ['name', "text"]
admin.site.register(Image, ImageAdmin)

'''
EXAMPLES OF ADMIN OPTIONS
class ActivityAdmin(admin.ModelAdmin):
	exclude =      ('slug', )
	list_display = (  'name', 'tags_as_list','level','is_published', '_get_link')
	list_filter =  ('is_published','level','tags',)
	search_fields = ['name', "preamble", "inspiration_text","resource_text", "tool_text"]
	filter_horizontal = ('tags','inspirations','resources','tools', "learnings")
	readonly_fields = [ "preview_image", ]
	actions = ['publish','set_fun','set_beginner', 'set_learner','set_expert']

	def preview_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width=350,
			height=250,
			)
	)
	def publish(modeladmin, request, queryset):
		queryset.update(is_published=True)
	publish.short_description = "Publish"





def get_picture_preview(obj):
	if obj.pk:  # if object has already been saved and has a primary key, show picture preview
		return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
			src=obj.image.url,
			title=obj.name,
		)
	return _("(choose a picture and save and continue editing to see the preview)")
get_picture_preview.allow_tags = True
get_picture_preview.short_description = "Picture Preview"

	'''
