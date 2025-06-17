from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class - allows editing CarModels directly from CarMake admin
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1  # Number of empty forms to display
    fields = ['name', 'model_type', 'year', 'engine', 'trim_level', 'base_price']
    ordering = ['-year']

# CarModelAdmin class - customization for CarModel admin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'model_type', 'year', 'base_price')
    list_filter = ('car_make', 'model_type', 'year')
    search_fields = ['name', 'car_make__name']
    ordering = ['-year', 'car_make', 'name']

# CarMakeAdmin class - includes CarModelInline for managing related models
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'founded_year', 'headquarters')
    search_fields = ['name', 'headquarters']
    list_filter = ('founded_year',)

# Register models with their custom admin classes
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
