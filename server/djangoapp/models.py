from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('HATCHBACK', 'Hatchback'),
        ('SUV', 'SUV'),
        ('COUPE', 'Coupe'),
        ('VAN', 'Van'),
        ('SEDAN', 'Sedan'),
        ('WAGON', 'Wagon')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(default=2023,
                                            validators=[
                                                MaxValueValidator(2023),
                                                MinValueValidator(2015)
    ])

    def __str__(self):
        return self.name
        
