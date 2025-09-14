# middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse

class CustomMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        response_data = {
            'error': str(exception),
            'status': 'error'
        }
        return JsonResponse(response_data, status=500)

    def process_request(self, request):
        # You can add custom request processing logic here
        pass

    def process_response(self, request, response):
        # You can add custom response processing logic here
        return response