from django.contrib import admin
from backlogger.models.mBackLogItem import BackLogItem


@admin.register(BackLogItem)
class BackLogItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'stage', 'created_at', 'updated_at', 'created_by')
