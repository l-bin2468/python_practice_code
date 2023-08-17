from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
import json

from jango.models import Info


# def list(request):
#     resp = request.body
#     json_result = json.loads(resp)
#     print(json_result)
#     return JsonResponse(json_result, status=200, safe=False)
#
#
# def testList(request):
#     resp = request.GET.get("page")
#     Info.objects.filter(id=3).delete()
#     print(resp)
#     return HttpResponse(resp)


def create(request):
    info = Info(name="1", total=1)
    info.save()

    Info.objects.create(name="2", total=2)

    dicts = {"name": "James", "total": 3}
    Info.objects.create(**dicts)
    print(Info.name)
    # =======================================
    goods_list = [{"name": "James", "total": 4}, {"name": "James", "total": 5}]
    queryset_list = []   # 创建列表，用与承载批量更新的对象数据
    for goods_data in goods_list:  # 用for循环遍历需要创建的数据列表，注：这里默认为列表内元素goods_data 是字典格式
        queryset_list.append(Info(**goods_data))  # 把创建元素添加到列表
    Info.objects.bulk_create(queryset_list)  # 批量创建
    # =======================================
    res_list = []
    newInfo = Info
    newInfo.name = "Jeff"
    newInfo.total = 10
    res_list.append(newInfo)
    print(res_list)
    for _, val in enumerate(res_list):
        print(val.name)
        print(val.total)
        Info.objects.create(name=val.name, total=val.total)
    # =======================================
    user_list = []
    for i in range(100):
        user_obj = Info(name='用户%s' % i, total=i)
        user_list.append(user_obj)
    Info.objects.bulk_create(user_list)
    return HttpResponse("OK")


def select(request):
    result = Info.objects.filter(id=2)  # filter()里可以用,分开 表示and
    print(result.get())
    for row in result:
        print(row.id, row.name)

    # 查询所有字段的所有值(元组)
    field_list = Info.objects.values_list()
    print(field_list)

    # 查询首个字段的所有值(列表)
    field_list = Info.objects.values_list(flat=True)
    print(field_list)

    # 查询所有字段的所有值(字典列表)
    field_list = Info.objects.values()
    print(field_list)

    # 查询某个字段的所有值(元组)
    field_list = Info.objects.values_list("name")
    print(field_list)

    res = Info.objects.values_list("total", "name")
    results = {}
    for val in res:
        key = val[0]
        value = val[1]
        try:
            results[key].append(value)
        except KeyError:
            results[key] = [value]
    print(results)
    return HttpResponse("OK")


def delete(request):
    Info.objects.filter(id=3).delete()
