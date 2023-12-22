"""
URL configuration for Obreque_Diego_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Seminario_APP import views

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Ruta para la página de inicio
    path('', views.index, name='index'),
    path('inscripcion/', views.nuevo_inscrito, name='add_inscrito'),

    # Rutas para las Class Based Views del modelo Inscrito
    path('inscritos/', views.InscritoListClass.as_view(), name='inscrito-list'),
    path('inscritos/<int:id>/', views.InscritoDetalleClass.as_view(), name='inscrito-detail'),

    # Rutas para las Function Based Views del modelo Institucion
    path('instituciones/', views.institucion_list, name='institucion-list'),
    path('instituciones/<int:id>/', views.institucion_detalle, name='institucion-detail'),
    path('institucion/', views.institucion_list, name='institucion_list'),
    path('institucion/nuevo/', views.nueva_institucion, name='nueva_institucion'),



]
