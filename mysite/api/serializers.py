from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Artist
        fields = ['url', 'id', 'owner', 'artist_name', 'first_name', 'last_name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(many=True, view_name='artist-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'artists']