
# Dokumentasi Proyek
## Di Susun Oleh : Raka Rendra Fayanto / L200224246

**web admin**

`username : admin`
`password : admin`

## Pendahuluan
Projek web untu membuat web menjadi modular atau memisahkan menjadi beberapa modul agar bisa di akses dari database

## Struktur Proyek
```
.
├── mywebsite
│   ├── contact
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── __pycache__
│   │   ├── templates
│   │   │   └── contact
│   │   │       ├── contact.html
│   │   │       └── response.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── mywebsite
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── Profile
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_profile_about_alter_profile_address_and_more.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── __pycache__
│   │   ├── templates
│   │   │   └── profile
│   │   │       ├── profile.html
│   │   │       └── resume.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── projects
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_remove_project_image.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── __pycache__
│   │   ├── templates
│   │   │   └── projects
│   │   │       ├── project_detail.html
│   │   │       └── projects.html
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static
│   │   └── css
│   │       └── base.css
│   └── templates
│       └── base.html
└── README.md

```
- **contact**: Aplikasi untuk mengelola kontak dan mengirimkan pesan.
- **Profile**: Aplikasi untuk menampilkan profil pengguna dan resume.
- **projects**: Aplikasi untuk mengelola dan menampilkan proyek yang telah dikerjakan.
- **static**: Folder untuk menyimpan file statis seperti CSS.
- **templates**: Folder untuk menyimpan template HTML.
- **mywebsite**: Folder utama yang berisi pengaturan proyek.

## Langkah-Langkah Pengembangan

### 1. Membuat Aplikasi
Aplikasi dibuat menggunakan perintah:
```bash
python manage.py startapp nama_aplikasi
```
Kami membuat tiga aplikasi: **contact**, **Profile**, dan **projects**.

### 2. Membuat Model
Di dalam setiap aplikasi, kami membuat model untuk mendefinisikan struktur data. Misalnya, pada aplikasi **projects**, kami membuat model `Project`:
```python
#projects/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
```
Model ini menyimpan informasi tentang proyek, seperti judul, deskripsi, tanggal mulai, dan tanggal selesai.

### 3. Mengatur Views
Kami menambahkan views di setiap aplikasi untuk mengatur logika. Contohnya, pada aplikasi **projects** kami memiliki view untuk menampilkan daftar proyek:
```python
#projects/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project

# View untuk menampilkan daftar proyek
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})

# View untuk menampilkan detail proyek berdasarkan id
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})
```

### 4. Menyusun URL
Setiap aplikasi memiliki file `urls.py` untuk mengatur URL routing. Misalnya, pada aplikasi **projects**, kami mengatur URL seperti berikut:
```python
#projects/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
]
```
URL ini akan mengarah ke view `project_list` yang menampilkan semua proyek.

### 5. Mengatur Setting
Kami juga mengonfigurasi `settings.py` untuk menambahkan aplikasi ke dalam `INSTALLED_APPS`:
```python
#prjects/settings.py
.
.
.
INSTALLED_APPS = [
    'Profile.apps.ProfileConfig',
    'projects.apps.ProjectsConfig',
    'contact.apps.ContactConfig',
]
```

### 6. Menggunakan Static CSS
Kami mengatur penggunaan file CSS statis di template `base.html` agar semua halaman memiliki navbar yang konsisten:
```html
<link rel="stylesheet" href="{% static 'css/base.css' %}">
```

### 7. Template
Kami menggunakan template untuk menyusun struktur halaman. Misalnya, pada `base.html`, kami menyusun menu navigasi dan bagian konten:
```html
#templates/base.html

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Website{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    {% block extra_css %}{% endblock %}
</head>
<body>      
    <header>
        <nav>
            <ul>
                <li><a href="{% url 'profile' %}">Home</a></li>
                <li><a href="{% url 'resume' %}">Resume</a></li>
                <li><a href="{% url 'project_list' %}">Projects</a></li>
                <li><a href="{% url 'contact' %}">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        {% block content %}
        {% endblock %}
    </main>
    <footer>
        &copy; {% now "Y" %} My Website
    </footer>   
</body>
</html>                 
```
### contoh menggunakan template di profil
```html
#projects/templates/profile/profile.html

{% extends 'base.html' %}

{% block title %}Profile - My Website{% endblock %}

{% block content %}
<h1>{{ profile.name }}</h1>
<p> Email           : {{ profile.email }}</p>
<p> No.             : {{ profile.phone }}</p>
<p> Alamat          : {{ profile.address }}</p>
<p> Tentang Saya    : {{ profile.about }}</p>
<p> Riwayat Sekolah : {{ profile.education }}</p>
<p> Pengalaman      : {{ profile.experience }}</p>
<p> Keterampilan    : {{ profile.skills }}</p>
{% endblock %}          
```