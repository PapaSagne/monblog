"""
URLs de l'application blog.
Chaque URL est reliée à une vue et possède un nom unique.
On y fait référence dans les templates avec {% url 'blog:nom' %}
"""

from django.urls import path
from . import views

# app_name permet de préfixer les noms : blog:article-list, blog:article-detail...
app_name = 'blog'

urlpatterns = [

    # Page d'accueil — liste des articles
    # URL : http://127.0.0.1:8000/
    path(
        '',
        views.ArticleListView.as_view(),
        name='article-list'
    ),

    # Détail d'un article
    # URL : http://127.0.0.1:8000/article/1/
    # <int:pk> capture l'identifiant de l'article dans l'URL
    path(
        'article/<int:pk>/',
        views.ArticleDetailView.as_view(),
        name='article-detail'
    ),

    # Créer un article (réservé à l'admin)
    # URL : http://127.0.0.1:8000/article/nouveau/
    path(
        'article/nouveau/',
        views.ArticleCreateView.as_view(),
        name='article-create'
    ),

    # Modifier un article (réservé à l'admin)
    # URL : http://127.0.0.1:8000/article/1/modifier/
    path(
        'article/<int:pk>/modifier/',
        views.ArticleUpdateView.as_view(),
        name='article-update'
    ),

    # Supprimer un article (réservé à l'admin)
    # URL : http://127.0.0.1:8000/article/1/supprimer/
    path(
        'article/<int:pk>/supprimer/',
        views.ArticleDeleteView.as_view(),
        name='article-delete'
    ),

]