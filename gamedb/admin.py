from django.contrib import admin
from .models import Detail, Game, Info, Rating, Requirement
from embed_video.admin import AdminVideoMixin

# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Game)
admin.site.register(Info, MyModelAdmin)
admin.site.register(Requirement)
admin.site.register(Detail)
admin.site.register(Rating)


# admin.site.register(Game, MyModelAdmin)