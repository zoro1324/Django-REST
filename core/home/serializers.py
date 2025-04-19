
from rest_framework import serializers

from .models import Person


class PersonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'

    def validate_age(self,age):
        if age<18:
            raise serializers.ValidationError('Age should be greater than 18')
        
        return age
    
    def validate_name(self,name):
        
        for c in name:
            if c.isalpha() or c ==' ':
                continue
            else:
                raise serializers.ValidationError("Non character values are not allowed.")
        
        return name