from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions
from api import serializers

from api.models import Artist
from api.serializers import UserSerializer, ArtistSerializer

from django.contrib.auth.models import User, Group

def index(request):
    return HttpResponse("hey")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def artist_detail(request, pk):
    """
    Retrieve, update or delete artist.
    """
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        artist.delete()
        return HttpResponse(status=204)

    
    return HttpResponse(status=404)