from rest_framework import routers
from .api import MASTERViewSets

router = routers.DefaultRouter()

router.register('master', MASTERViewSets, 'master')

urlpatterns = router.urls