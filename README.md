# 📝 MonBlog — Projet Django

Un blog fonctionnel développé avec le framework **Django**.  
Réalisé dans le cadre du Master MICDA à l'UNCHK.

---

## ✨ Fonctionnalités

- 📋 Liste des articles avec pagination
- 📖 Lecture complète d'un article
- ✏️ Créer, modifier, supprimer des articles (admin uniquement)
- 🖼️ Upload et affichage d'images
- 🔐 Authentification administrateur
- 🎨 Design élégant sombre et doré

---

## 🏗️ Structure du projet
```
monblog/
├── blog/
│   ├── models.py       ← Modèle Article
│   ├── views.py        ← 5 Class-Based Views
│   ├── urls.py         ← URLs de l'application
│   └── admin.py        ← Administration personnalisée
├── monblog/
│   ├── settings.py     ← Configuration du projet
│   └── urls.py         ← URLs principales
├── templates/
│   ├── base.html       ← Template parent
│   └── blog/
│       ├── article_list.html
│       ├── article_detail.html
│       ├── article_form.html
│       └── article_confirm_delete.html
├── static/
│   └── css/
│       └── style.css   ← Feuille de styles
├── manage.py
└── requirements.txt
```

---

## 🚀 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/VOTRE_USERNAME/monblog.git
cd monblog
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

Ouvrir **http://127.0.0.1:8000** dans le navigateur.

---

## 🔑 Accès administration

- URL : `http://127.0.0.1:8000/admin/`
- Identifiants par défaut :
  - **Utilisateur** : `admin`
  - **Mot de passe** : `admin1234`

---

## 📊 Modèle Article

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

## 🎯 Class-Based Views

| Vue | URL | Rôle |
|-----|-----|------|
| `ArticleListView` | `/` | Liste des articles |
| `ArticleDetailView` | `/article/<pk>/` | Détail d'un article |
| `ArticleCreateView` | `/article/nouveau/` | Créer un article |
| `ArticleUpdateView` | `/article/<pk>/modifier/` | Modifier un article |
| `ArticleDeleteView` | `/article/<pk>/supprimer/` | Supprimer un article |

---

## 👨‍💻 Technologies

- **Python 3** + **Django 6**
- **SQLite** — base de données
- **Pillow** — traitement des images
- **HTML5 / CSS3** — templates et styles
- **Google Fonts** — Playfair Display + Inter

---

## 📬 Contact

Projet soumis à :
- abdourahmane.balde@unchk.edu.sn
- master.micda@unchk.edu.sn