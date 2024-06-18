from django.shortcuts import render
from django.views import View
from .models import Services, ServieCategory, ServiceDoctor, SerivePrice


class ServiceView(View):
    template_name = "pages/service/services-2.html"
    
    def get_context_data(self):
        context = {
            "services" : Services.objects.all()
        }
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

class ServiceDetailView(View):
    template_name = "pages/service/service_detail.html"

    
    def get_context_data(self, *args, **kwargs):
        context = {
            "service" : Services.objects.get(slug= self.kwargs["slug"])
        }
        return context
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)


def service_category_deteaile(request, slug):
    context = {}
    context['objects'] = ServieCategory.objects.get(slug=slug)
    context['services'] = Services.objects.all()
    return render(request, 'pages/service/category.html', context)