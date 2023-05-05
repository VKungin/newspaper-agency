from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from agency.models import Redactor, Topic, Newspaper


class NewspaperAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "published_date"]


admin.site.register(Redactor, UserAdmin)
admin.site.register(Topic)
admin.site.register(Newspaper, NewspaperAdmin)
