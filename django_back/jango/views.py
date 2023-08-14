from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json


def list(request):
    resp = request.body
    json_result = json.loads(resp)
    print(json_result)
    return JsonResponse(json_result)


def testList(request):
    resp = request.GET.get("page")
    # json_result = json.loads(resp)
    print(resp)
    return HttpResponse(resp)

