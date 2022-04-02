from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('artists/', views.ArtistList.as_view()),
    path('artists/<int:pk>/', views.ArtistDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', views.api_root),
]

# urlpatterns = format_suffix_patterns(urlpatterns)