from rest_framework import serializers
from .models import YourOpening, YourRepertiore

class YourOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourOpening
        fields = ('id', 'opening_name', 'opening_moves', 'opening_sequence')
        
class YourRepertioreSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourOpening
        fields = ('id', 'repertiore_moves', 'repertiore_sequence')
  
        