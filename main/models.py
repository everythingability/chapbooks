from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from urllib.parse import urlparse
from urllib.parse import parse_qs

from ckeditor.fields import RichTextField

# Not just pages but also text fragements used throughout the site
class Image(models.Model):
	''
	image = models.ImageField(upload_to ='', 
			height_field=None, width_field=None, max_length=250,
			blank=True, default=None, null=True)
	url = models.URLField(max_length=250)
	previewURL = models.URLField(max_length=250)
	downloadURL = models.URLField(max_length=250)
	order = models.IntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return str(self.image)
	
	def fix(self):
		#http://www-users.york.ac.uk/~tas509/chapbooks/9943182670001381_08.jpg
		try:
			u = self.previewURL.replace("http:", "https:")
			self.previewURL = u
			print(u)
			self.save()
			#
			parts = u.split("_")
			part = parts[1]
			num = int(part.split(".")[0])
			print(num)
			self.order = num
			self.save()
		except Exception as err:
			print(err)



	class Meta:
		ordering = ['order',]


class Chapbook(models.Model):
	''
	name = models.CharField(max_length=250)
	mmsid = models.IntegerField(null=True, blank=True, default=0)
	preamble = RichTextField(default='', null=True, blank=True,)
	text = RichTextField(null=True, blank=True, default='')
	images = models.ManyToManyField('Image', blank=True,  )
	publish = models.BooleanField(default=True)

	def __str__(self):
		return str(self.name)



class Page(models.Model):
	slug = models.SlugField(null=True, blank=True, default='')
	name = models.CharField(max_length=250)
	preamble = RichTextField(default='', null=True, blank=True,)
	image = models.ImageField(upload_to ='', 
			height_field=None, width_field=None, max_length=250,
			blank=True, default=None, null=True)
	#tags = models.ManyToManyField('Tag', blank=True,  )
	#category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="category1")
	#image_url = models.URLField(max_length=250, null=True, default='', blank=True)
	#youtube = models.URLField(max_length=250, null=True, default='', blank=True)

	text = RichTextField(null=True, blank=True, default='')

	class Meta:
		ordering = ['name',]

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Page, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
	'''
	def _get_thumbnail(self):
		return format_html(u'<img src="{}" width="150"/>', self.image_url)
	_get_thumbnail.allow_tags = True


	'''

class Tag(models.Model):
	slug = models.SlugField(null=True, blank=True, default='')
	name = models.CharField(max_length=100)
	about = models.TextField(null=True, blank=True, default='')
	class Meta:
		ordering = ['name',]

	def __str__(self):
		return self.name

	'''def tools_count(self):
		tagC = Tool.objects.filter(tags=self).count()
		resC = Resource.objects.filter(tags=self).count()
		inspC = Inspiration.objects.filter(tags=self).count()
		return tagC + resC + inspC

	def font_size(self):
		return translate(self.tools_count(), 0, 100, 12, 48 )'''

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Tag, self).save(*args, **kwargs)