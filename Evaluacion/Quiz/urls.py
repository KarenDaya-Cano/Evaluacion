from django.urls import path
from Quiz import views

urlpatterns = [
    path('',views.Tabla, name='tabla'),
]
