from django.db import models
from django.utils.translation import gettext as _

class Squirrels(models.Model):
    TRUE = 'true'
    FALSE = 'false'
    AM = 'AM'
    PM = 'PM'
    ADULT = 'adult'
    JUVENILE = 'juvenile'
    BLANK = ''
    UNKNOWN = '?'
    BLACK = 'black'
    CINNAMON = 'cinnamon'
    GRAY = 'gray'
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    OTHER = 'other'

    BOOL_CHOICES = (
            (TRUE, 'True'),
            (FALSE, 'False'),
        )
    
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
        )
    
    AGE_CHOICES = (
            (ADULT, 'Adult'),
            (JUVENILE, 'Juvenile'),
            (BLANK, ''),
            (UNKNOWN, '?'),
        )

    COLOR_CHOICES = (
            (BLACK, 'Black'),
            (CINNAMON, 'Cinnamon'),
            (GRAY, 'Gray'),
        )

    LOC_CHOICES = (
            (GROUND_PLANE, ' Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            (OTHER, 'Other'),
        )
    
    Unique_Squirrel_Id = models.CharField(
            max_length=30,
            help_text=_("Unique Squirrel ID"),
        )
    
    Latitude = models.FloatField(help_text=_("Latitude"),)

    Longitude = models.FloatField(help_text=_("Longitude"),)

    Shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
            help_text=_("Shift"),
        )

    Date = models.DateField(
            help_text=_("Date"),
        )

    Age = models.CharField(
            max_length=50,
            choices=AGE_CHOICES,
            help_text=_("Age"),
        )

    Location = models.CharField(
            max_length=100,
            choices=LOC_CHOICES,
            default=OTHER,
            help_text=_("Location"),
        )

    Specific_Location = models.CharField(
            max_length=30,
            help_text=_("Specific Location"),
        )

    Primary_Fur_Color = models.CharField(
            max_length=20,
            choices=COLOR_CHOICES,
            help_text=_("Primary Fur Color"),
        )
    
    Running = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Running'),
            )

    Chasing = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Chasing'),
            )


    Climbing = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Climbing'),
            
            )

    Eating = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Eeating'),
            )

    Foraging = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Foraging'),
            )

    Other_Activities = models.CharField(
            max_length=100,
            help_text=_('Other activities'),
            )

    Kuks = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Kuks'),
            )

    Quaas = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Quaas'),
            )

    Moans = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Moan'),
            )

    Tail_flags = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Tail Flags'),
            )

    Tail_twitches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Tail Twitch'),
            )

    Approaches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Approaches'),
            )

    Indifferent = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Indifferent'),
            )

    Runs_from = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Run from'),
        )
    def __str__(self):
        return self.Unique_Squirrel_Id

