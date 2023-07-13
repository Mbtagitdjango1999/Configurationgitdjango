from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models.mixins import TitleSlugMixin,TimestampMixin,BannerOperationMixin,TitleSlugDescriptionMixin,PictureOperationMixin
 

class Post(TimestampMixin,TitleSlugDescriptionMixin,PictureOperationMixin):
    summary = models.CharField(_("Summary"),)
    priority = models.PositiveSmallIntegerField(_("Priority"), )
    picture = models.ImageField(_("Picture"),upload_to="blog/post",width_field="pic_width_field",height_field="pic_height_field",max_length=110)
    category = models.ForeignKey("PostCategory",verbose_name="Category",on_delete=models.PROTECT,related_name='posts',help_text=_("access to all post by category"))
    tags = models.ManyToManyField('PostTag',verbose_name="Tags",related_name='posts',help_text=_("access to all posts by tags"))
    
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    
    
class PostCategory(TitleSlugMixin,TimestampMixin) :
    class Meta :
        verbose_name = _("Post Category")
        verbose_name_plural = _("Post Categories") 
          
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    
    
class PostTag(TitleSlugMixin,TimestampMixin) :
    class Meta :
        verbose_name = _("Post Tag")
        verbose_name_plural = _("Posts Tags") 
          
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title    
    