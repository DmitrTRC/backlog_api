from django.db import models
from django.contrib.auth.models import User


class BackLogItem(models.Model):
    title = models.CharField('title', max_length=200, blank=False, null=False)
    description = models.TextField('description', blank=True, null=True)
    is_done = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='backlog_items')

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        ordering = ['-created_at']
