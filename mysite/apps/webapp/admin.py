from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from .models import *


class ContactAdmin(admin.ModelAdmin):

    list_display = ( 'firstName', 'lastName', 'email', 'company', 'phone', 'case' )
    # list_display_links = ('id', 'name')
    # search_fields = ('name',)
    list_per_page = 25

class ServicesContactAdmin(admin.ModelAdmin):

    list_display = ( 'firstName', 'lastName', 'email', 'question')
    # list_display_links = ('id', 'name')
    # search_fields = ('name',)
    list_per_page = 25


admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ServicesContact, ServicesContactAdmin)
admin.site.register(Litigation)
admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(Subscribe)




