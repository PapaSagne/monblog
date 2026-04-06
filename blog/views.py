

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
# LISTE DES ARTICLES — Page d'accueil
# ============================================================
class ArticleListView(ListView):
    
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'  
    paginate_by = 6                  

    def get_queryset(self):
        
        return Article.objects.filter(statut=Article.STATUT_PUBLIE)

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['total_articles'] = Article.objects.filter(
            statut=Article.STATUT_PUBLIE
        ).count()
        return context


# ============================================================
# DÉTAIL D'UN ARTICLE — Lecture complète
# ============================================================
class ArticleDetailView(DetailView):
    
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        
        if self.request.user.is_staff:
            return Article.objects.all()
        return Article.objects.filter(statut=Article.STATUT_PUBLIE)


# ============================================================
# CRÉER UN ARTICLE
# ============================================================
class ArticleCreateView(LoginRequiredMixin, CreateView):
    
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['titre', 'auteur', 'resume', 'contenu', 'image', 'statut', 'date_publication']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre_page'] = 'Nouvel article'
        context['bouton_texte'] = "Publier l'article"
        return context

    def form_valid(self, form):
        messages.success(
            self.request,
            f'✅ L\'article "{form.instance.titre}" a été créé avec succès !'
        )
        return super().form_valid(form)


# ============================================================
# MODIFIER UN ARTICLE
# ============================================================
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    
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
# SUPPRIMER UN ARTICLE
# ============================================================
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    
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