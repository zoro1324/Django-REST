
from rest_framework import serializers
from .models import Person,Color
import matplotlib.colors as mcolors




class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializers(serializers.ModelSerializer):
    color = ColorSerializers()
    color_code = serializers.SerializerMethodField()

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
    
    def get_color_code(self,obj):
        
        color_obj = Color.objects.get(id=obj.color.id)
        color_name = color_obj.color_name
        color_code = mcolors.to_hex(color_name)

        return {"color_code":color_code}
