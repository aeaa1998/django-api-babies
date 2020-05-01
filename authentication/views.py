from django.shortcuts import render
import json
import jwt
from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login(request):
    try:
        username = request.POST['username']
        password =  request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            encoded_jwt = jwt.encode({
                    'username': user.username,
                    'iat': datetime.utcnow(),
                    'nbf': datetime.utcnow() + timedelta(minutes=-5),
                    'exp': datetime.utcnow() + timedelta(days=7)
                }, '123456', algorithm='HS256')
            return HttpResponse(encoded_jwt)
        else:
            return HttpResponse(json.dumps({"invalid_credentials" : "Wrong username and password combination" }), 412)
    except (KeyError) as e:
        return HttpResponse(json.dumps({"errorMessage" : "Missing username or password" }), 412)
    except IndexError:
        return HttpResponse(json.dumps({"invalid_credentials" : "Wrong username and password combination" }), 412)


