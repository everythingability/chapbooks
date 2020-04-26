from django.core.management.base import BaseCommand, CommandError
from main.models import *

import csv, os
import os.path
from os import path

dir_path = os.path.dirname(os.path.realpath(__file__))
class Command(BaseCommand):
    # python manage.py import_tools file="tools.csv"
    help = 'meant to help me get started, importing a lot of initial data etc'

    def add_arguments(self, parser):
        ''
        #parser.add_argument('file',  type=str)

    def handle(self, *args, **options):
        #filename  = options['file']
        try:
           chapbooks = Chapbook.objects.all()

           for chapbook in chapbooks:
               print(chapbook.name)
               for image in chapbook.images.all():
                    f = image.image
                    fullpath = "/Users/tomsmith/mydjangoapps/chapbooks/uploads/" + str(f)
                    doesExist = path.exists( str(fullpath) )
                    if (doesExist):
                       ''
                       print(doesExist)
                    else:
                      print(doesExist, fullpath)
                      chapbook.images.remove(image)

                        

     

              
        except Exception as err:
            raise CommandError( str(err))

        self.stdout.write(self.style.SUCCESS('Done!'))