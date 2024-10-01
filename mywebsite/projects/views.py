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