from django.urls import path
from Seminario_APP import views

app_name = 'Seminario_APP'

urlpatterns = [
    path('', views.index, name='index'),
    # Rutas de Inscrito
    path('inscritos/', views.InscritoListClass.as_view(), name='inscrito-list'),
    path('inscritos/<int:id>/', views.InscritoDetalleClass.as_view(), name='inscrito-detail'),
    path('inscripcion/', views.InscritoCreateView.as_view(), name='add_inscrito'),
    
    # Rutas de Institucion
    path('instituciones/', views.institucion_list, name='institucion-list'),
    path('instituciones/<int:id>/', views.institucion_detalle, name='institucion-detail'),
    path('institucion/nuevo/', views.nueva_institucion, name='nueva_institucion'),
]
