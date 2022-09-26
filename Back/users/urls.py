from rest_framework import routers
from .views import USERViewSets
from django.urls import path

router = routers.SimpleRouter()

router.register('login', USERViewSets, 'login')

urlpatterns = router.urls