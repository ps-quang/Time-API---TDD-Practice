# times/views.py
from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone


def time_api(request):
    return JsonResponse({
        'current_time': timezone.now().strftime(settings.DATETIME_FORMAT)
    })