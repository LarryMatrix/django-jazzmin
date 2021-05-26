from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
   FacilityView
)

router = DefaultRouter()

router.register('create', FacilityView)

app_name = 'facility'

urlpatterns = [
    path('', include(router.urls)),
]
