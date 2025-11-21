from django.urls import path,include
from rest_framework import routers
from .views import CategoryViewSets,ProductViewSets


router = routers.DefaultRouter()
router.register(r'category',CategoryViewSets)
router.register(r'product',ProductViewSets)


urlpatterns = [
    path('',include(router.urls))
]