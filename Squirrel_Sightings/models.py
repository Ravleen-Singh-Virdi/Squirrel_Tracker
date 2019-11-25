from django.db import models
from django.utils.translation import gettext as _

###We are missing location and specific location in this model
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

    Latitude = models.IntegerField()

    Longitude = models.IntegerField()

    Unique_Squirrel_Id = models.CharField(
            max_length=30,
            help_text=_("Squirrel's Unique ID"),
        )

    Shift = models.CharField(
            max_length=2,
            choices=SHIFT_CHOICES,
        )

    Date = models.DateField(
            help_text=_("Date of the sighting"),
        )

    Age = models.CharField(
            max_length=50,
            choices=AGE_CHOICES,
            help_text=_("Age of the Squirrel"),
        )

    Primary_Fur_Color = models.CharField(
            max_length=20,
            choices=COLOR_CHOICES,
            help_text=_("Color of the squirrel"),
        )
    
    Running = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it running?'),
            )

    Chasing = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it chasing?'),
            )


    Climbing = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it climbing?'),
            
            )

    Eating = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it eating?'),
            )

    Foraging = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('is it foraging?'),
            )

    Other_Activities = models.CharField(
            max_length=100,
            help_text=_('What other activities is it doing?'),
            )

    Kuks = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it kuks?'),
            )

    Quaas = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it quaas?'),
            )

    Moans = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it moan?'),
            )

    Tail_flags = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it flag its tail?'),
            )

    Tail_twitches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it twitch its tail?'),
            )

    Approaches = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it approach?'),
            )

    Indifferent = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Is it indifferent?'),
            )

    Runs_from = models.CharField(
            max_length=20,
            choices=BOOL_CHOICES,
            help_text=_('Does it run away?'),
        )







# Create your models here.
