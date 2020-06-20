from django.contrib import admin
from board.models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):  # describes how must looks post in admin panel

    def get_post_str(self, obj):
        pass

    get_post_str.short_description = 'Some short description'
    pass


admin.site.register(Rubric)
admin.site.register(Post)