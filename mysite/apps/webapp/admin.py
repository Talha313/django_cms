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

# class FlsaPlaceholderAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
#     # Editable fields
#     frontend_editable_fields = ("title", "content", "url")
#     # Form fields order and sections
#     fieldsets = [
#         (None,{"fields" : ["title", "url"]})
#     ]

class FLSAAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass



admin.site.register(About)
admin.site.register(Contact, ContactAdmin)
admin.site.register(ServicesContact, ServicesContactAdmin)
admin.site.register(Litigation)
admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(Subscribe)
# admin.site.register(FlsaClaim, FlsaClaimAdmin)

admin.site.register(FlsaClaim, FLSAAdmin)



