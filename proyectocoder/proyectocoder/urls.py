"""proyectocoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familias/', views.familias_lista, name='familias_lista'),
    path('familias/agregar/', views.familia_agregar, name='familia_agregar'),
    path('familias/<int:pk>/editar/', views.familia_editar, name='familia_editar'),
    path('familias/<int:pk>/eliminar/', views.familia_eliminar, name='familia_eliminar'),
    path('familias/<int:pk>/miembros/agregar/', views.miembro_agregar, name='miembro_agregar'),
    path('familias/<int:pk>/miembros/<int:miembro_pk>/eliminar/', views.miembro_eliminar, name='miembro_eliminar'),
    path('familias/', include('familia.urls')),
]


