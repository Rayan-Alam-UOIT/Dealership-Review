from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    headquarters = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"


# Car Model model
class CarModel(models.Model):
    # Car types
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]
    
    # Fields
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model_type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default='SUV'
    )
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )
    engine = models.CharField(max_length=50, null=True, blank=True)
    trim_level = models.CharField(max_length=50, null=True, blank=True)
    color_options = models.CharField(max_length=200, null=True, blank=True)
    base_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
    
    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"
        ordering = ['-year', 'car_make', 'name']
