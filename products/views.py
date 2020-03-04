from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserdetailsSerializer
from .models import Userdetails

class UserdetailsViewSet(viewsets.ModelViewSet):
    queryset = Userdetails.objects.all()
    serializer_class = UserdetailsSerializer
