from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user_manager.models import CustomUser


class Note(models.Model):
    name = models.CharField(max_length=150)
    url_image = models.URLField(default='No disponible', null=True, blank=True) 
    
    def __str__(self):
        return self.name
   

class Brand(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


TIME_OF_DAY = [
    ('d','day'),
    ('n', 'night'),
    ('t', 'total')
]

SEASONS_OF_YEAR = [
    ('S','summer'),
    ('F', 'fall'),
    ('W', 'winter'),
    ('p', 'spring'),
]

class Fragrance(models.Model):
    url_image = models.URLField(default='No disponible', blank=True, null=True)
    name = models.CharField( max_length=250)
    concentration = models.CharField(max_length=50, default='Desconocido')
    brand = models.ForeignKey(Brand, verbose_name='brand',on_delete=models.CASCADE)
    top_notes = models.ManyToManyField(Note, related_name='note_top', verbose_name='top_notes')
    middle_notes = models.ManyToManyField(Note, related_name='note_middle', verbose_name='middle_notes')
    base_notes = models.ManyToManyField(Note, related_name='note_base', verbose_name='base_notes')
    time_of_day = models.CharField( max_length=1, choices=TIME_OF_DAY)
    seasons_of_year = models.CharField( max_length=1, choices=SEASONS_OF_YEAR)
    rating_admin = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    comment_admin = models.TextField()

    def __str__(self):
        return self.name


class Collection(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email


class Item(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    parfum = models.ForeignKey(Fragrance, on_delete=models.CASCADE)
    rating_user = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment_user = models.TextField(null=True, blank=True)
    
    class Meta:
        unique_together = ('collection', 'parfum')

    def __str__(self):
        return self.parfum.name