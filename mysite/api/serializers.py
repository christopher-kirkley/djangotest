from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Artist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    artist_letter = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = ['url', 'id', 'owner', 'artist_letter', 'artist_name', 'first_name', 'last_name']

    def get_artist_letter(self, instance):
        return str(instance.artist_name)[0]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    artists = serializers.HyperlinkedRelatedField(many=True, view_name='artist-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'artists']