# convert any specified models to JSON for FE API easy access

from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo # the model to work with
        fields = ('id', 'title', 'description', 'completed') # the fields to be converted to JSON
