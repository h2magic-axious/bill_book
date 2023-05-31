# from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


#
# import orjson
#
# class CMiddleware(MiddlewareMixin):
#     @staticmethod
#     def process_request(request):
#         path = request.path
#         if "login" in path:
#             pass
#
class CloseCsrfMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(self, request):
        request.csrf_processing_done = True
