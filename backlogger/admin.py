from django.contrib import admin
from backlogger.models.mBackLogItem import BackLogItem


@admin.register(BackLogItem)
class BackLogItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_done', 'created_at', 'is_important')
