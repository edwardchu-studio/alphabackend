
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

import json
'''
Dealing with requsts

'''

from alphabrain.InterGame import InterGame,InterGameTest

HUMAN_FIRST=-1
HUMAN_SECOND=1
game=InterGame()


@csrf_exempt
def index(request):
    rtn = {"status": "failed"}
    if request.method == "POST":
        rtn["status"]="success"
        rtn["msg"]="POST succeed"
    if request.method == "GET":
        rtn["status"]="success"
        rtn["msg"]="GET succeed"
    return HttpResponse(json.dumps(rtn))

@csrf_exempt
def init(request):
    rtn = {"status": "failed"}
    if request.method == "POST":
        game.board=game.game.getInitBoard()
        
        rtn["status"]="success"
        rtn["msg"]="init succeed"
        print("Game initialized")
    return HttpResponse(json.dumps(rtn))

@csrf_exempt
def next(request):

    rtn = {"status": "failed"}
    if request.method == "POST":
        rtn["status"]="success"
        print(request.POST)

        humanMove=(request.POST.get("humanMove[r]",(0,0)),request.POST.get("humanMove[c]",(0,0)))

        print(humanMove)
        assert(len(humanMove)==2)

        game.HumanPlay(humanMove)
        print("Human makes a move: {}".format(humanMove))
        game.showBoard()
        result=game.judgeGame()
        _curScore=game.getScore()
        print("Score after human move:{}".format(_curScore))
        if result!=0:
            #game ends
            print("{} won.".format("Human" if result==1 else "Alpha"))
            rtn["result"]="Human" if result==1 else "Alpha"
            rtn['AlphaMove']=None
            return HttpResponse(json.dumps(rtn))

        print("shifted to alphaaaaa")
        #Time for Alpha
        alphaMove=game.getAlphaPlayFromCache(humanMove)
        result=game.judgeGame()
        print(alphaMove,type(alphaMove),type(alphaMove[0]))
        game.showBoard()
        _curScore=game.getScore()
        print("Score after alpha move:{}".format(_curScore))
        if result!=0:
            print("{} won.".format("Human Wins!" if result==1 else "Alpha Wins!"))
            rtn["result"]="Human Wins!" if result==1 else "Alpha Wins!"
            rtn['AlphaMove']=None
            return HttpResponse(json.dumps(rtn))
        else:
            rtn["result"]="Continues"
            rtn['AlphaMove']=alphaMove
            return HttpResponse(json.dumps(rtn))


@csrf_exempt
def getInfo(request):

    rtn = {"status": "failed"}
    if request.method == "GET":
        print(request)
        rtn["status"]="success"
        key=request.GET['query']




    return HttpResponse(json.dumps(rtn))
