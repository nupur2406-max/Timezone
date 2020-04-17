import pytz
from django.utils import timezone
from django.http import JsonResponse
import logging
from myapp.models import Country

# Get an instance of a logger

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    # def process_request(request):
    #     print('inside middleware')
    #     print(request)
    #     return JsonResponse({'message': 'from middleware'})


    def __call__(self, request):
        if('Country' not in request.headers or request.headers['Country']==''):
            return JsonResponse({'message': 'Country Name Not Found.'})
        try:
            country = Country.objects.get(name=request.headers['Country'])
        except:
            return JsonResponse({'message': 'Invalid country name'})
        if ('Timezone' not in request.headers or request.headers['Timezone'] == ''):
            return JsonResponse({'message': 'Timezone Not Found.'})
        if(country.timezone != request.headers['Timezone']):
            return JsonResponse({'message': 'Timezone mismatch'})

        return self.get_response(request)

# class TimezoneMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.translations = {
#             "en": {"India": "Asia/Kolkata", "header": "check timezone!"},
#             "nl": {"greeting": "Hallo", "header": "Welkom Django!"},
#         }
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response
#
#     def process_template_response(self, request, response):
#         response.context_data["translations"] = self.translations
#         return response