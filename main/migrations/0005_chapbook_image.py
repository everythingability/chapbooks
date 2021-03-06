# Generated by Django 3.0.5 on 2020-04-25 10:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200424_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, max_length=250, null=True, upload_to='')),
                ('url', models.URLField(max_length=250)),
                ('downloadURL', models.URLField(max_length=250)),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('preamble', ckeditor.fields.RichTextField(blank=True, default='/%Y/%m/%d', null=True)),
                ('text', ckeditor.fields.RichTextField(blank=True, default='', null=True)),
                ('images', models.ManyToManyField(blank=True, to='main.Image')),
            ],
        ),
    ]
