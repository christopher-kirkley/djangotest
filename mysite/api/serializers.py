from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Artist


class UserSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'artists']


"""Refactor to use ModelSerializer"""
class ArtistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Artist
        fields = ['artist_name', 'first_name', 'last_name', 'owner']

class UserSerializer(serializers.ModelSerializer):
    artists = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'artists']