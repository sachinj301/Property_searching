from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ['realtor', 'title', 'address', 'city', 'state', 'zipcode', 'description',
                    'price', 'bedrooms', 'bathrooms', 'garage', 'sqrt', 'lot_size',
                    'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
                    'is_published',  'list_date']

admin.site.register(Listing,ListingAdmin)

