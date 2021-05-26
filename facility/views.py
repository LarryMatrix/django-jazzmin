from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from .serializers import FacilitySerializer
from rest_framework.permissions import IsAuthenticated
from .models import Facility


User = get_user_model()


# Create your views here.
class FacilityView(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,)
    http_method_names = ['post']

