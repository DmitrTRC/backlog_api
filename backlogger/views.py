from rest_framework import viewsets, permissions, filters
from .models.mBackLogItem import BackLogItem
from backlogger.serializers.api.task import BackLogItemSerializer


class BackLogItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows backlog items to be viewed or edited.
    """
    queryset = BackLogItem.objects.all()
    serializer_class = BackLogItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_fields = ['priority']

    def perform_create(self, serializer):
        """
        Create a new backlog item.
        :param serializer:
        :return:
        """
        # Set the created_by field to the current user.
        serializer.save(created_by=self.request.user)
