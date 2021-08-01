from rest_framework import serializers
from rest_framework.utils import field_mapping

from .models import MobileModel

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','name', 'desc','company', 'date_creation')
        model = MobileModel
        