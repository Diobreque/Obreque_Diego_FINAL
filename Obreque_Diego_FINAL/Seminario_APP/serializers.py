from rest_framework import serializers
from Seminario_APP import models


class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inscrito
        fields = '__all__'


class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'
