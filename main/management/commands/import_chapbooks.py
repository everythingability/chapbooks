from django.core.management.base import BaseCommand, CommandError
from main.models import *

import csv, os

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
            #self.stdout.write(dir_path)
            #self.stdout.write(filename)
            filename = "new_chapbooks.csv"
            fullpath = dir_path + "/" + filename
            self.stdout.write(fullpath)
            thumbs_path = "/Users/tomsmith/mydjangoapps/chapbooks/main/static/images/thumbnails"
            
            file = open(fullpath, 'r')
            reader = csv.DictReader(file)
            for i,rec in enumerate(reader):
                #title,mmsid,titles,urls,viewlinks
                try:
                    name = rec["title"]
                    mmsid = rec["mmsid"]
                    titles = rec["titles"].split(",")
                    titles.reverse()
                    urls = rec["urls"]
                    viewlinks = rec["viewlinks"].split(",")
                    viewlinks.reverse()

                    chabookObj, created = Chapbook.objects.get_or_create(name=name)
                    chabookObj.mmsid = mmsid

                    if created:
                        chabookObj.save()

                    self.stdout.write(str(i) + ": " + name + " "  + mmsid)
                    for n,title in enumerate(titles):
                        title = title.replace(".jpf", ".jpg")
                        self.stdout.write("\t" + title)
                        fpath = thumbs_path + "/" + title
                        self.stdout.write(fpath)
                        #self.stdout.write(os.path.isfile(fpath))

                        
                        imgObj, created = Image.objects.get_or_create(image="thumbnails/" + title)
                        if created:
                            url = viewlinks[n]
                            url = url.replace("['", "")
                            url = url.replace("'", "")
                            imgObj.url = url
                            imgObj.order = n
                            imgObj.save()
                        chabookObj.images.add( imgObj)

                    chabookObj.save()
                    self.stdout.write("\n")

                except Exception as err:
                    self.stdout.write( "Error: " + str(err) + " name" )

        except Exception as err:
            raise CommandError( str(err))

        self.stdout.write(self.style.SUCCESS('Done!'))