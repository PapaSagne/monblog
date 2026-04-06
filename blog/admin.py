

from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    

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

    # Champs remplis automatiquement
    readonly_fields = ('date_creation', 'date_modification')

    # Organisation des champs en sections
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'auteur', 'resume', 'contenu')
        }),
        ('Image', {
            'fields': ('image',),
            'classes': ('collapse',),  
        }),
        ('Publication', {
            'fields': ('statut', 'date_publication')
        }),
        ('Informations automatiques', {
            'fields': ('date_creation', 'date_modification'),
            'classes': ('collapse',),
        }),
    )