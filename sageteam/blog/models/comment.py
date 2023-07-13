from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user
from painless.models.mixins import TitleSlugMixin,TimestampMixin,BannerOperationMixin,TitleSlugDescriptionMixin,PictureOperationMixin
  
    #TODO asdasdas
class Comment(TimestampMixin) :
    class Meta :
        verbose_name = _("Post Comment")
        verbose_name_plural = _("Post Comment") 
        
    text = models.TextField(_("Text"),max_length=500,help_text=_("Text content of the comment"))
    post = models.ForeignKey("Post" , on_delete=models.CASCADE,related_name='comments',help_text=_("Access to all comments from a post"))
    reply = models.ForeignKey("self",verbose_name=_("Reply"),on_delete=models.CASCADE,related_name="replies",help_text=_("Access to all reply frpm a comment"))
    user = models.ForeignKey(get_user,)    
          
    def __str__(self) -> str:
        return self.title
    def __repr__(self) -> str:
        return self.title
    