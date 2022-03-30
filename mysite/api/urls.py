from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('artists/', views.artist_list),
    path('artists/<int:pk>/', views.artist_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]