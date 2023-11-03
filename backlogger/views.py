from rest_framework import viewsets, permissions
from .models.mBackLogItem import BackLogItem
from backlogger.serializers.api.task import BackLogItemSerializer


class BackLogItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows backlog items to be viewed or edited.
    """
    queryset = BackLogItem.objects.all()
    serializer_class = BackLogItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the created_by field to the current user.
        serializer.save(created_by=self.request.user)
