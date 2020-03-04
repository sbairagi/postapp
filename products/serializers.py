from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import Userdetails

class UserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Userdetails
        fields = ('id','fname','lname','email','username','password')