import pytest
from api.models import Artist, Track

from django.contrib.auth.models import User, Group

@pytest.mark.django_db
def test_user_model():
    queryset = User.objects.all()
    assert len(queryset) == 0

@pytest.mark.django_db
def test_can_add_track():
    track = Track(track_name='Potato')
    track.save()
    queryset = Track.objects.all()
    assert len(queryset) == 1

@pytest.mark.django_db
def test_artist_new(mocker):
    mock_creator = mocker.patch("Artist.create")






