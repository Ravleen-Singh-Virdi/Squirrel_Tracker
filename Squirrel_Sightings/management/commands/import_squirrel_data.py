import csv
import os
import datetime as dt
from django.core.management.base import BaseCommand, CommandError
from Squirrel_Sightings.models import Squirrels
from django.conf import settings

class Command(BaseCommand):
    help = 'Import csv data into database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', help ='path of csv data')


    def import_data_from_csv(self, filename):
        with open(filename, 'r') as csv_file:
            data = csv.reader(csv_file, delimiter=',')
            headers = next(data)
            for data_object in data:
                Latitude = data_object[0]
                Longitude = data_object[1]
                Unique_Squirrel_Id = data_object[2]
                Shift = data_object[3]
                Date = dt.datetime.strptime(data_object[4].strip(),'%m%d%Y').date()
                Age = data_object[5]
                Primary_Fur_Color = data_object[6]
                Location = data_object[7]
                Specific_Location = data_object[8]
                Running = True if "true" in data_object[9].lower() else False
                Chasing = True if "true" in data_object[10].lower() else False
                Climbing = True if "true" in data_object[11].lower() else False
                Eating = True if "true" in data_object[12].lower() else False
                Foraging = True if "true" in data_object[13].lower() else False
                Other_Activities = True if "true" in data_object[14].lower() else False
                Kuks = True if "true" in data_object[15].lower() else False
                Quaas = True if "true" in data_object[16].lower() else False
                Moans = True if "true" in data_object[17].lower() else False
                Tail_flags = True if "true" in data_object[18].lower() else False
                Tail_twitches = True if "true" in data_object[19].lower() else False
                Approaches = True if "true" in data_object[20].lower() else False
                Indifferent = True if "true" in data_object[21].lower() else False
                Runs_from = True if "true" in data_object[22].lower() else False                
                try:
                    sighting, created = Squirrels.objects.get_or_create(
			Latitude=Latitude,
                        Longitude=Longitude,
                        Unique_Squirrel_Id=Unique_Squirrel_Id,
			Shift=Shift,
        		Date=Date,
                        Age=Age,
                        Primary_Fur_Color=Primary_Fur_Color,
                        Location=Location,
                        Specific_Location=Specific_Location,
                        Running=Running,
                        Chasing=Chasing,
                        Climbing=Climbing,
                        Eating=Eating,
                        Foraging=Foraging,
                        Other_Activities=Other_Activities,
                        Kuks=Kuks,
                        Quaas=Quaas,
                        Moans=Moans,
                        Tail_flags=Tail_flags,
                        Tail_twitches=Tail_twitches,
                        Approaches=Approaches,
                        Indifferent=Indifferent,
                        Runs_from=Runs_from
                    )
                    if created:
                        sighting.save()
                        display_format = "\nSquirrel_Sighting, {}, has been saved."
                        print(display_format.format(sighting))
                except Exception as ex:
                    print(str(ex))

    def handle(self, *args, **options):
        file_path = options['file_path']
        self.import_data_from_csv(file_path)

