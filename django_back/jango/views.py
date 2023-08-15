from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json

from jango.models import Info


def list(request):
    resp = request.body
    json_result = json.loads(resp)
    print(json_result)
    return JsonResponse(json_result)


def testList(request):
    resp = request.GET.get("page")
    Info.objects.filter(id=3).delete()
    print(resp)
    return HttpResponse(resp)


def create(request):
    info = Info(name="1")
    info.save()

    Info.objects.create(name="2")

    dicts = {'name': "James"}
    Info.objects.create(**dicts)
    print(Info.name)
    return HttpResponse("OK")


def select(request):
    result = Info.objects.filter(id=2)  # filter()里可以用,分开 表示and
    print(result.get())
    for row in result:
        print(row.id, row.name)

    return HttpResponse("OK")

