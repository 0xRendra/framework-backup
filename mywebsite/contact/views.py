from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Simpan data ke dalam model Contact
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Redirect ke halaman response atau sukses dengan data yang diperlukan
        return redirect('response', name=name, email=email, message=message)
    
    return render(request, 'contact/contact.html')

def response_view(request, name, email, message):
    context = {
        'name': name,
        'email': email,
        'message': message,
    }
    return render(request, 'contact/response.html', context)  # Pastikan ada template response.html
