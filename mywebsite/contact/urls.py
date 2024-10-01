from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('response/<str:name>/<str:email>/<str:message>/', views.response_view, name='response'),
]