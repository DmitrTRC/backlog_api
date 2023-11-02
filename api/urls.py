from django.urls import path, include
from api.spectacular.urls import urlpatterns as doc_urls

from backlogger.urls import urlpatterns as backlogger_urls

app_name = 'api'

# The API URLs are now determined automatically by the router.
urlpatterns = [

    # path('auth/', include('djoser.urls.base')),
    path('auth/', include('djoser.urls.jwt')),

]

urlpatterns += doc_urls
urlpatterns += backlogger_urls
