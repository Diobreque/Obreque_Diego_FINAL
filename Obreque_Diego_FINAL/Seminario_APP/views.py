from django.shortcuts import render, redirect
from .serializers import InscritoSerializer, InstitucionSerializer
from .models import Inscrito, Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import get_object_or_404



# Create your views here.

def index(request):
    context = {
        'title': 'Inicio - Seminario Gastronómico',
        'accion': 'Bienvenidos al Seminario de Gastronomía'
    }
    return render(request, 'index.html', context)

# Class Based Views para Inscrito
class InscritoListClass(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetalleClass(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(pk=id)
        except Inscrito.DoesNotExist:
            raise Http404

    def get(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data)

    def put(self, request, id):
        inscrito = self.get_object(id)
        serializer = InscritoSerializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Function Based Views para Institucion
@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InstitucionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
    try:
        institucion = Institucion.objects.get(pk=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InstitucionSerializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
