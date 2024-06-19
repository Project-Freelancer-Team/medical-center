from django.shortcuts import render
from django.views import View
from service.models import Services
from django.http import JsonResponse
import openai
from django.conf import settings
from .models import Reviews



class HomeView(View):
    template_name = "index.html"
    
    def get_context_data(self):
        context = {
            "services" : Services.objects.all(),
            "reviews" : Reviews.objects.all()
        }
        print(context["reviews"])
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    

class ReviewView(View):
    template_name = "review.html"
    
    def get_context_data(self):
        context = {}
        return context
    
    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self, request):
        context = self.get_context_data()
        if "review" in request.POST:
            name = request.POST.get("name")
            person_job = request.POST.get("person_job")
            body = request.POST.get("body")
            object = Reviews.objects.create(
                name = name,
                person_job = person_job,
                body = body
            )
        return render(request, self.template_name, context)
    

def contact(request):
    return render(request, 'pages/contact.html')
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def consult(request):
    openai.api_key = settings.OPENAI_API_KEY
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_message}
                ]
            )
            gpt_message = response.choices[0].message['content'].strip()
            return JsonResponse({'message': gpt_message})
    return render(request, 'pages/consult.html')