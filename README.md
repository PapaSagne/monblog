# MonBlog — Projet Django

## Fonctionnalités

-Liste des articles avec pagination
-Lecture complète d'un article
-Créer, modifier, supprimer des articles (admin uniquement)
-Upload et affichage d'images
-Authentification administrateur

## Accès administration

- URL : `http://127.0.0.1:8000/admin/`
- Identifiants par défaut :
  - **Utilisateur** : `admin`
  - **Mot de passe** : `admin1234`


## Modèle Article

| Champ | Type | Description |
|-------|------|-------------|
| `titre` | CharField | Titre de l'article |
| `contenu` | TextField | Corps du texte |
| `resume` | TextField | Courte description |
| `auteur` | CharField | Nom de l'auteur |
| `image` | ImageField | Image illustrative |
| `statut` | CharField | brouillon ou publié |
| `date_publication` | DateTimeField | Date de publication |

---

## Class-Based Views

| Vue | URL | Rôle |
|-----|-----|------|
| `ArticleListView` | `/` | Liste des articles |
| `ArticleDetailView` | `/article/<pk>/` | Détail d'un article |
| `ArticleCreateView` | `/article/nouveau/` | Créer un article |
| `ArticleUpdateView` | `/article/<pk>/modifier/` | Modifier un article |
| `ArticleDeleteView` | `/article/<pk>/supprimer/` | Supprimer un article |

---

## Technologies

- **Python 3** + **Django 6**
- **SQLite** — base de données
- **Pillow** — traitement des images
- **HTML5 / CSS3** — templates et styles
- **Google Fonts** — Playfair Display + Inter

---
