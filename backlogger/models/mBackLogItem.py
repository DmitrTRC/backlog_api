from django.db import models
from django.contrib.auth.models import User


class BackLogItem(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    STAGE_CHOICES = [
        ('BL', 'Backlog'),
        ('TD', 'To Do'),
        ('IP', 'In Progress'),
        ('DN', 'Done'),
    ]

    title = models.CharField('title', max_length=200, blank=False, null=False)
    description = models.TextField('description', blank=True, null=True)
    priority = models.CharField('priority', max_length=1, choices=PRIORITY_CHOICES, default='L')
    stage = models.CharField('stage', max_length=2, choices=STAGE_CHOICES, default='BL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                                   related_name='backlog_items')

    def __str__(self):
        return f'{self.title} - {self.description}'

    class Meta:
        ordering = ['-created_at']
