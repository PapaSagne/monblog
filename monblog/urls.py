"""
URLs principales du projet MonBlog.
Ce fichier est le point d'entrée de toutes les URLs du site.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Interface d'administration Django
    # URL : http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # URLs de l'application blog
    # Le préfixe '' signifie que le blog est à la racine du site
    path('', include('blog.urls')),

]

# En développement, Django sert lui-même les images uploadées
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )