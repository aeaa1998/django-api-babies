from guardian.shortcuts import assign_perm
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpResponse
from parents.models import Parent, Baby
from events.models import Event
from parents.serializers import ParentSerializer, BabySerializer
from permissions.services import APIPermissionClassFactory
from events.serializers import EventSerializer
from rest_framework.decorators import action

class ParentsViewSet(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    @action(detail=False, url_path='(?P<pk>\d+)/babies', methods=['get'])
    def getBabiesByParentId(self, request, pk=None):
        babies =  Baby.objects.filter(parent__pk=pk)
        serializer_context = {'request': Request(request._request)}
        return Response(BabySerializer(babies, many= True,context=serializer_context).data)

class BabiesViewSet(viewsets.ModelViewSet):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer

    def retrieve(self, request, pk=None):
        try:
            baby =  Baby.objects.get(pk=pk)
            if request.user.has_perm('parents.see_baby', baby):
                serializer_context = {'request': Request(request._request)}
                return Response(BabySerializer(baby, context=serializer_context).data)
            else:
                return Response("You do not have permission to perform this action.", 404)
        except (Exception) as e:
            return Response("invalid", 404)

    @action(detail=False, url_path='(?P<pk>\d+)/events', methods=['get'])
    def retrieveEventsbyBaby(self, request, pk=None):
        events = Event.objects.filter(baby__pk=pk)
        if request.user.has_perm('parents.see_baby', Baby.objects.get(pk=pk)):
            serializer_context = {'request': Request(request._request)}
            return Response(EventSerializer(events, many=True,context=serializer_context).data)
        else:
            return Response("You do not have permission to perform this action.", 404)

    def create(self, request):
        try:
            lastName = request.POST['last_name']
            firstName =  request.POST["first_name"]
            baby = Baby(first_name=firstName, last_name=lastName, parent=request.user.parent)
            baby.save()
            assign_perm('events.add_event', request.user)
            assign_perm('parents.change_baby', request.user, baby)
            assign_perm('parents.see_baby', request.user, baby)
            serializer_context = {'request': Request(request._request)}
            return Response(BabySerializer(baby, context=serializer_context).data)
        except (KeyError) as e:
            return HttpResponse(json.dumps({"errorMessage" : "missing_fields"}), 412)
