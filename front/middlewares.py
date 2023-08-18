from django.http import HttpResponse
from rest_framework.authtoken.models import Token

from front.models import Option


class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        token = request.headers.get('Authorization')
        if token:
            token = token.split()[1]
        if (not path.startswith('/admin')):
            maintenance_mode = Option.get_option("maintenance_mode", 'no')
            if maintenance_mode == "yes":
                response = HttpResponse("در حال بروزرسانی", status=503)
                return response

        response = self.get_response(request)
        return response