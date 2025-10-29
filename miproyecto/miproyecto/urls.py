from django.contrib import admin
from django.urls import path
from miapp import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.saludo),  # Ruta para la vista saludo
    path("datos/", views.info),  # Ruta para la vista info
]

