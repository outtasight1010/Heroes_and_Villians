from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'name','alter_ego','primary_ability','secondary_ability','catch_phrase']
        
        