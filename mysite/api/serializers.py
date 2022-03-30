from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Artist

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# class ArtistSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True) 
#    artist_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#    first_name = serializers.CharField(required=False, allow_blank=True, max_length=100)
#    last_name = serializers.CharField(required=False, allow_blank=True, max_length=100)

#    def create(self, validated_data):
#        """
#        Create a new 'artist' instance given the data
#        """
#        return Artist.objects.create(**validated_data)
       
#    def update(self, instance, validated_data):
#        instance.artist_name = validated_data.get('artist_name', instance.artist_name)
#        instance.first_name = validated_data.get('first_name', instance.first_name)
#        instance.last_name = validated_data.get('last_name', instance.last_name)
#        instance.save()
#        return instance 


"""Refactor to use ModelSerializer"""
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['artist_name', 'first_name', 'last_name']
