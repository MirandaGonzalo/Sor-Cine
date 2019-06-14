from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^compra/', compra, name="compra"),
    url(r'^datos_pelicula/(?P<id_pelicula>\d+)$', datos_pelicula, name="datos_pelicula"),
    url(r'^compra_entradas/(?P<id_pelicula>\d+)$', compra_entradas, name="compra_entradas"),
    url(r'^admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

