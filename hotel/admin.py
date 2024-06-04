from django.contrib import admin
from .models import Room, Hotel, Booking


admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Hotel)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_type', 'price', 'floor', 'balcony',)
    search_fields = ('number', 'room_type', 'hotel__name')


class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'phone', 'email')
    search_fields = ('name', 'city', 'country')
