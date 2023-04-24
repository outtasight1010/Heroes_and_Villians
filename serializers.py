from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name','alter_ego','primary_ability','secondary_ability','catch_phrase','type_of_super']
        
        
