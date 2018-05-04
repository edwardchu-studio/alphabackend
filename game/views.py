
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import json
'''
Dealing with requsts

'''

# from ..alphabrain.InterGame import InterGame

HUMAN_FIRST=-1
HUMAN_SECOND=1
# game=InterGame(order=HUMAN_FIRST)

@csrf_exempt
def index(request):
    rtn = {"status": "failed"}
    if request.method == "POST":
        rtn["status"]="success"

    return HttpResponse(json.dumps(rtn))

@csrf_exempt
def init(request):
    rtn = {"status": "failed"}
    if request.method == "POST":
        print(request)
        rtn["status"]="success"

    return HttpResponse(json.dumps(rtn))

@csrf_exempt
def next(request):

    rtn = {"status": "failed"}
    if request.method == "POST":
        print(request)
        rtn["status"]="success"
        humanMove=request.GET['humanMove']
        # game.HumanPlay(humanMove)
        print(humanMove)

        #return alpha moved
        # alphaMove=game.AlphaPlay()


    return HttpResponse(json.dumps(rtn))



@csrf_exempt
def getInfo(request):

    rtn = {"status": "failed"}
    if request.method == "GET":
        print(request)
        rtn["status"]="success"
        key=request.GET['query']




    return HttpResponse(json.dumps(rtn))
