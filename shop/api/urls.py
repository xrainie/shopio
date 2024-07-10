from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.api import views

app_name = 'shop'

router = DefaultRouter()
router.register('shop', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
