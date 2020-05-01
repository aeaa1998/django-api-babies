from rest_framework import serializers
from parents.models import Baby, Parent
class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name']

class BabySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Baby
        fields = ['id', 'first_name', 'last_name']


