# -*- encoding: utf-8 -*-
# Author: Komorebi
# Date: 2023/8/16 22:42
# Describe:
import datetime

from django.http import HttpResponse

from jango.models import Info


def create():
    info = Info(name="1")
    info.save()

    Info.objects.create(name="2")

    dicts = {'name': "James"}
    Info.objects.create(**dicts)
    print(Info.name)
    return HttpResponse("OK")


def select():
    result = Info.objects.filter(id=2)  # filter()里可以用,分开 表示and
    print(result.get())
    for row in result:
        print(row.id, row.name)

    return HttpResponse("OK")


def handle_time():
    # windows 和 linux 时间戳转换时，可能会受时区影响
    dt = datetime.datetime.now()
    dt.astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S")
