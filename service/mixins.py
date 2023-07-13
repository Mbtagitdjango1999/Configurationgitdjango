from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    class Meta :
        abstract = True
        
    
    created = models.DateTimeField(_("Created"),auto_now_add=True,help_text='auto insertion')
    modified = models.DateTimeField(_("Modified"),auto_now=True,help_text='auto mification')
        



class  PictureOperationMixin(models.Model):
    
    class Meta :
        abstract = True
    
    pic_height_field = models.PositiveSmallIntegerField(
        null=True,blank=True,editable=False,help_text="Size of Picture's height"
    )
    
    pic_width_field = models.PositiveSmallIntegerField(
        null=True,blank=True,editable=False,help_text="Size of Picture's width"
    )
    
    pic_alternate_text = models.CharField(
        max_length=110,
        help_text= 'Description about picture that is uploaded.'
    )       
    
    
    

class  BannerOperationMixin(models.Model):
    
    class Meta :
        abstract = True
    
    banner_height_field = models.PositiveSmallIntegerField(
        null=True,blank=True,editable=False,help_text="Size of Picture's height"
    )
    
    banner_width_field = models.PositiveSmallIntegerField(
        null=True,blank=True,editable=False,help_text="Size of Picture's width"
    )
    
    banner_alternate_text = models.CharField(
        max_length=110,
        help_text= 'Description about picture that is uploaded.'
    )           