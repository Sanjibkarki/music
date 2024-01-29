from rest_framework import serializers
from .models import Album

class Myserializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id','favourites']