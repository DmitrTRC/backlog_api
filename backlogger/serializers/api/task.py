from rest_framework import serializers
from backlogger.models.mBackLogItem import BackLogItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class BackLogItemSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = BackLogItem
        fields = [
            'id', 'title', 'description', 'priority', 'stage',
            'created_at', 'updated_at', 'created_by'
        ]
