from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.resgister = (r'products', views.ProductViewSet)


urlspattern = [
    path('api/', include('router.urls')),
]