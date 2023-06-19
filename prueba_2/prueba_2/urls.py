from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import (mostrar_principal, 
mostrar_precios,
mostrar_historial,
mostrar_recuerdos
)
urlpatterns = [
    path('',mostrar_principal,name='mostrar_principal'),
    path('', include('m_usuario.urls')),
    path('precios/', mostrar_precios, name='mostrar_precios'),
    path('historial/',mostrar_historial,name='mostrar_historial'),
    path('recuerdos/',mostrar_recuerdos,name='mostrar_recuerdos'),
    path('notas/', include('m_publicacion.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
