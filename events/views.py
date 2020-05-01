import json
from django.http import HttpResponse
from events.models import Event, Type as EventType
from guardian.shortcuts import assign_perm
from parents.models import Baby
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions
from events.serializers import EventSerializer, TypeSerializer
from permissions.services import APIPermissionClassFactory

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.parent.babies.filter(pk=req.POST["baby_id"]),
                    'retrieve': lambda user, req:  Event.objects.filter(baby__parent__user__pk=req.user.id).exists(),
                },
                'instance': {

                }
            }
        ),
    )
    def retrieve(self, request, pk=None):
        try:
            event =  Event.objects.get(pk=pk, baby__parent__user__pk=request.user.id)
            serializer_context = {'request': Request(request._request)}
            return Response(EventSerializer(event, context=serializer_context).data)
        except (Exception) as e:
            return Response("invalid_event_id", 404)

    def list(self, request):
        events =  Event.objects.filter(baby__parent__user__pk=request.user.id)
        serializer_context = {'request': Request(request._request)}
        return Response(EventSerializer(events, many= True,context=serializer_context).data)

    def create(self, request):
        try:
            babyId =  request.POST["baby_id"]
            if request.user.has_perm('events.add_event'):
                eventTypeId = request.POST['event_type_id']
                comment =  request.POST.get("comment", "")
                event = Event(comment=comment, baby=Baby.objects.get(pk=babyId), event_type=EventType.objects.get(pk=eventTypeId))
                event.save()
                assign_perm('events.change_event', request.user, event)
                assign_perm('events.see_event', request.user, event)
                serializer_context = {'request': Request(request._request)}
                return Response(EventSerializer(event, context=serializer_context).data)
            else:
                return HttpResponse(json.dumps({"errorMessage" : "does_now_have_perm"}), 412)
        except (KeyError) as e:
            return HttpResponse(json.dumps({"errorMessage" : "missing_fields"}), 412)
        except (Baby.DoesNotExist):
            return HttpResponse(json.dumps({"errorMessage" : "baby does not belongs to you or does not exist"}), 404)
        except (EventType.DoesNotExist):
            return HttpResponse(json.dumps({"errorMessage" : "invalid event type"}), 404)


class TypesViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = TypeSerializer
