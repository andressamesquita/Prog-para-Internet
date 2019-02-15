from rest_framework import serializers
from shortner.models import *

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Url
        fields = ('texto_url',)