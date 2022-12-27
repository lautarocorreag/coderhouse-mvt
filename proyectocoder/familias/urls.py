from django.urls import path
from . import views

urlpatterns = [
    path('', views.familias_lista, name='familias_lista'),
    path('agregar/', views.familia_agregar, name='familia_agregar'),
    path('<int:pk>/editar/', views.familia_editar, name='familia_editar'),
    path('<int:pk>/eliminar/', views.familia_eliminar, name='familia_eliminar'),
    path('<int:pk>/miembros/agregar/', views.miembro_agregar, name='miembro_agregar'),
    path('<int:pk>/miembros/<int:miembro_pk>/eliminar/', views.miembro_eliminar, name='miembro_eliminar'),
]
