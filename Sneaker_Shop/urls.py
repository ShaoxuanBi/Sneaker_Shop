# The total routing
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # The back-end
    path('', include("Glasneaker.urls")),  # Front-end: Imports subroute files into the current total route file for easy management
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
