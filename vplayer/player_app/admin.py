# from django.contrib import admin
 
# Register your models here.
# from .models import Video
 
# admin.site.register(Video)


from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)