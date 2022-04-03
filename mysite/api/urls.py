import imp
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

from api.views import ArtistViewSet, UserViewSet

router = DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
   path('', include(router.urls))
]

# artist_list = ArtistViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# artist_detail = ArtistViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#    path('', views.api_root),
#    path('artists/', artist_list, name='artist-list'),
#    path('artists/<int:pk>/', artist_detail, name='artist-detail'),
#    path('users/', user_list, name='user-list'),
#    path('users/<int:pk>/', user_detail, name='user-detail'),

# ]

# urlpatterns = format_suffix_patterns(urlpatterns)