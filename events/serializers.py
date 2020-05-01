from events.models import Event, Type
from rest_framework import serializers
class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    event_type = TypeSerializer()
    class Meta:
        model = Event
        fields = ['id', 'comment', 'event_type']


