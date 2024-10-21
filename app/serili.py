
from rest_framework import serializers
from . models import *

class Itemajax(serializers.ModelSerializer):
    class Meta:
        model = shippment
        fields ='__all__'
class Itemahistort(serializers.ModelSerializer):
    class Meta:
        model = shippmenthistory
        fields ='__all__'

