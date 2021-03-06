import csv
import datetime as dt
  
from django.core.management.base import BaseCommand

from Squirrel_Sightings.models import Squirrels
from django.conf import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        for item in data:
            try:    
                s = Squirrels(
                    Unique_Squirrel_Id = item['\ufeffUniqueSquirrelID'],
                    Latitude = item['Latitude'],
                    Longitude = item['Longitude'],
                    Shift = item['Shift'],
                    Date = dt.datetime.strptime(item['Date'].strip(),'%m%d%Y').date(),
                    Age = item['Age'],
                    Primary_Fur_Color = item['PrimaryFurColor'],
                    Location = item['Location'],
                    Specific_Location = item['SpecificLocation'],
                    Running = item['Running'],
                    Chasing = item['Chasing'],
                    Climbing = item['Climbing'],
                    Eating = item['Eating'],
                    Foraging = item['Foraging'],
                    Other_Activities = item['OtherActivities'],
                    Kuks = item['Kuks'],
                    Quaas = item['Quaas'],
                    Moans = item['Moans'],
                    Tail_flags = item['Tailflags'],
                    Tail_twitches = item['Tailtwitches'],
                    Approaches = item['Approaches'],
                    Indifferent = item['Indifferent'],
                    Runs_from = item['Runsfrom'],
                )
                s.save()
                print('Item ',{s},' has been saved')	
            except Exception as ex:
                print('Error:',str(ex))
