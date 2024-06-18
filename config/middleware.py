from django.shortcuts import redirect, render
from service.models import Services

def all_service(get_res):
    def middleware(request):
        request.all_service = Services.objects.all()
        response = get_res(request)
        # request.get_description = SeoContent.objects.all()
        # response = get_res(request)
        return response
    return middleware