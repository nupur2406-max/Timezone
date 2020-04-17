from django.shortcuts import redirect, render
import pytz
from django.http import JsonResponse
# Create your views here.


def set_timezone(request):
    return JsonResponse({'message': 'middleware check pass'})