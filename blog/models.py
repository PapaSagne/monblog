

from django.db import models
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
   
    # Choix possibles pour le statut de l'article 
    STATUT_BROUILLON = 'brouillon'
    STATUT_PUBLIE = 'publie'
    CHOIX_STATUT = [
        (STATUT_BROUILLON, 'Brouillon'),  # Non visible par les visiteurs
        (STATUT_PUBLIE, 'Publié'),         # Visible par tout le monde
    ]

    # Titre de l'article 
    titre = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )

    #  Corps du texte de l'article 
    contenu = models.TextField(
        verbose_name="Contenu"
    )

    # Courte description affichée dans la liste 
    resume = models.TextField(
        blank=True,  
        verbose_name="Résumé"
    )

    # Nom de l'auteur 
    auteur = models.CharField(
        max_length=100,
        verbose_name="Auteur"
    )

    # Image illustrative de l'article 
    image = models.ImageField(
        upload_to='articles/',  
        blank=True,             
        null=True,
        verbose_name="Image"
    )

    # Statut 
    statut = models.CharField(
        max_length=20,
        choices=CHOIX_STATUT,
        default=STATUT_BROUILLON,  # Par défaut = brouillon
        verbose_name="Statut"
    )

    # Date de publication  
    date_publication = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date de publication"
    )

    # Date de création
    date_creation = models.DateTimeField(
        auto_now_add=True,  
        verbose_name="Date de création"
    )

    # Date de dernière modification
    date_modification = models.DateTimeField(
        auto_now=True, 
        verbose_name="Dernière modification"
    )

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-date_publication']  # Du plus récent au plus ancien

    def __str__(self):
        """Texte affiché pour représenter l'article (dans l'admin par exemple)."""
        return self.titre

    def get_absolute_url(self):
        """Retourne l'URL de la page de détail de cet article."""
        return reverse('blog:article-detail', kwargs={'pk': self.pk})