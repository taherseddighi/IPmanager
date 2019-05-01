from django.shortcuts import render
from json import JSONEncoder
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Available_Public_IP


# Create your views here.

@csrf_exempt
def submit_Available_Public_IP(request):
    #validate data later
    #this_token = request.POST['token']
    #this_user = User.objects.filter(token__token=this_token).get()
    #now = datetime.now()
    #Available_Public_IP.objects.Create(User=this_user, IP=request.POST['IP'], date_start=now)
    print('HI Can you See Me ? I am Here. Holllaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(request.POST)

    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder)