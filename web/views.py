from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import User, Token

# Create your views here.

@csrf_exempt
def submit_Available_Public_IP(request):
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    
    
    print('HI')
    print(request.POST)

    return JsonResponse({
        'status':'ok',
    }, encoder=JSONEncoder)