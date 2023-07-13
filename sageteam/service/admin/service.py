from django.contrib import admin
#from ..models.service import Service 
from sageteam.service.models import Service
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'summary',
        'created',
        'modified',
                    )
    
    search_fields = (
        'title',
        'summary',
        'description',
    )
    
    search_help_text =_("Search by kon taghar and  title,summary,description")
    
    list_filter = (
        'created',
        'modified',
    )
    
    save_on_top =True
    
    
    
    fieldsets = (
        
        (_("Service Information"),{'classes':('collapse',),"fields":('title',
        'summary',
        'description')}),
        
           (_("Picture Management"),{'classes':('collapse',),"fields":('icon',
            'picture',
            'pic_alternate_text',
            'banner',
            'banner_alternate_text',
            'pic_width_field',
            'pic_height_field',
            'banner_width_field',
            'banner_height_field'
            
            
        )}),
        
        (_("Security Center"),{'classes':('collapse',),"fields":( 'created',
        'modified')}),
        
    )
    
    readonly_fields = (
           'created',
           'modified',
           'pic_width_field',
           'pic_height_field',
           'banner_width_field',
           'banner_height_field'
         
            )
    
    