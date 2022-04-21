from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json

def helloWorld(request):
    now  = datetime.now()
    return HttpResponse("oh, hi! current server time is{now}".format(now=str(now)))
 

def blackpink(request):
    # import pdb; pdb.set_trace()
    numbers = request.GET['numbers']
    return HttpResponse("this page is for blackpink")


def hi(request):
    numbers = map(lambda x : int(x),request.GET["numbers"].split(","))
    return JsonResponse({ "numbers" : sorted(numbers)},json_dumps_params={'indent': 4})

def sorted(request):
    numbers =  [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succsessfully'
    }

    return HttpResponse(json.dumps(data, indent=4),
            content_type = 'application/json')

def say_hi(request, name, age):
    if age >= 18:
        return HttpResponse(f"Bien venido {name} !!!")
    return HttpResponse(f"Sorry {name} this page is only for 18 years!")


