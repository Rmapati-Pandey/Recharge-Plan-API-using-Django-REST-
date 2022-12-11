from rest_framework import serializers
from api.models import Company
from api.models import Plans
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
        read_only_fields = [f.name for f in model._meta.get_fields()]


class PlansSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model=Plans
        fields='__all__'