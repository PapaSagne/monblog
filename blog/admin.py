"""
Configuration de l'interface d'administration Django.
Ce fichier contrôle comment les articles apparaissent dans /admin/
"""

from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Personnalisation de l'affichage du modèle Article dans l'admin.
    Le décorateur @admin.register() enregistre le modèle automatiquement.
    """

    # Colonnes affichées dans la liste des articles
    list_display = ('titre', 'auteur', 'statut', 'date_publication')

    # Filtres dans la barre latérale droite
    list_filter = ('statut', 'auteur', 'date_publication')

    # Champs utilisés pour la barre de recherche
    search_fields = ('titre', 'contenu', 'auteur')

    # Navigation par date en haut de la liste
    date_hierarchy = 'date_publication'

    # Tri par défaut : du plus récent au plus ancien
    ordering = ('-date_publication',)

    # Champs modifiables directement dans la liste
    list_editable = ('statut',)

    # Nombre d'articles par page dans l'admin
    list_per_page = 20

    # Champs remplis automatiquement (non modifiables)
    readonly_fields = ('date_creation', 'date_modification')

    # Organisation des champs en sections dans le formulaire
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'auteur', 'resume', 'contenu')
        }),
        ('Image', {
            'fields': ('image',),
            'classes': ('collapse',),  # Section rétractable
        }),
        ('Publication', {
            'fields': ('statut', 'date_publication')
        }),
        ('Informations automatiques', {
            'fields': ('date_creation', 'date_modification'),
            'classes': ('collapse',),
        }),
    )