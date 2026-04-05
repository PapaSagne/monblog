"""
Vues du blog — les 5 Class-Based Views (CBV) requises.

ListView   → afficher la liste des articles
DetailView → afficher un seul article en détail
CreateView → formulaire pour créer un article
UpdateView → formulaire pour modifier un article
DeleteView → page de confirmation pour supprimer un article
"""

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Article


# ============================================================
# 1. LISTE DES ARTICLES — Page d'accueil
# ============================================================
class ArticleListView(ListView):
    """
    Affiche la liste de tous les articles publiés.
    Django cherche automatiquement le template : blog/article_list.html
    La variable {{ articles }} sera disponible dans le template.
    """
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'  # Nom de la variable dans le template
    paginate_by = 6                   # 6 articles par page maximum

    def get_queryset(self):
        """
        On filtre uniquement les articles publiés.
        Les brouillons ne sont pas visibles par les visiteurs.
        """
        return Article.objects.filter(statut=Article.STATUT_PUBLIE)

    def get_context_data(self, **kwargs):
        """
        On ajoute des données supplémentaires au template.
        """
        context = super().get_context_data(**kwargs)
        context['total_articles'] = Article.objects.filter(
            statut=Article.STATUT_PUBLIE
        ).count()
        return context


# ============================================================
# 2. DÉTAIL D'UN ARTICLE — Lecture complète
# ============================================================
class ArticleDetailView(DetailView):
    """
    Affiche un seul article identifié par son id (pk) dans l'URL.
    Django cherche automatiquement le template : blog/article_detail.html
    La variable {{ article }} sera disponible dans le template.
    """
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        """
        Les visiteurs voient uniquement les articles publiés.
        L'admin connecté peut voir tous les articles.
        """
        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.objects.filter(statut=Article.STATUT_PUBLIE)


# ============================================================
# 3. CRÉER UN ARTICLE
# ============================================================
class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
    Affiche un formulaire pour créer un nouvel article.
    LoginRequiredMixin : redirige vers /admin/login/ si non connecté.
    Django cherche automatiquement le template : blog/article_form.html
    """
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'auteur', 'resume', 'contenu', 'image', 'statut', 'date_publication']

    def get_context_data(self, **kwargs):
        """On passe le titre de la page et le texte du bouton au template."""
        context = super().get_context_data(**kwargs)
        context['titre_page'] = 'Nouvel article'
        context['bouton_texte'] = "Publier l'article"
        return context

    def form_valid(self, form):
        """Appelé quand le formulaire est valide. On affiche un message de succès."""
        messages.success(
            self.request,
            f'✅ L\'article "{form.instance.titre}" a été créé avec succès !'
        )
        return super().form_valid(form)


# ============================================================
# 4. MODIFIER UN ARTICLE
# ============================================================
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """
    Affiche un formulaire pré-rempli pour modifier un article existant.
    Récupère l'article par son id (pk) dans l'URL.
    Utilise le même template que CreateView : blog/article_form.html
    """
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'auteur', 'resume', 'contenu', 'image', 'statut', 'date_publication']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre_page'] = f'Modifier : {self.object.titre}'
        context['bouton_texte'] = 'Enregistrer les modifications'
        context['est_modification'] = True
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            f'✅ L\'article "{form.instance.titre}" a été mis à jour !'
        )
        return super().form_valid(form)


# ============================================================
# 5. SUPPRIMER UN ARTICLE
# ============================================================
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """
    Affiche une page de confirmation avant de supprimer un article.
    Django cherche automatiquement le template : blog/article_confirm_delete.html
    Après suppression, redirige vers la liste des articles.
    """
    model = Article
    template_name = 'blog/article_confirm_delete.html'
    context_object_name = 'article'
    # reverse_lazy() car les URLs ne sont pas encore chargées au démarrage
    success_url = reverse_lazy('blog:article-list')

    def form_valid(self, form):
        titre = self.object.titre
        messages.success(
            self.request,
            f'🗑️ L\'article "{titre}" a été supprimé.'
        )
        return super().form_valid(form)