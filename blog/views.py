from django.shortcuts import render
from django.views import View

from .models import BlogPost, Tags
from .filter_functions import filter_by_name

from django.core.paginator import Paginator


class BlogMainView(View):
    template_name = "pages/blog/blog-2-col.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {}
        posts = BlogPost.objects.all()
        current_page = self.request.GET.get('page', 1)
        paginator = Paginator(posts, 4) 

        try:
            page_obj = paginator.page(current_page)
        except paginator.PageNotAnInteger:
            page_obj = paginator.page(1)
        except paginator.EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context['posts'] = page_obj
        context['page_obj'] = page_obj
        context['paginator'] = paginator

        return context
    
    def get(self,request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self,request, *args, **kwargs):
        context = self.get_context_data()
        if "filter" in request.POST:
            context["posts"] = filter_by_name(request, request.POST.get("title"))
        return render(request, self.template_name, context)


class BlogDetailView(View):
    template_name = "pages/blog/blog-details.html"
    
    def get_context_data(self, *args, **kwargs):
        context = {}
        context["blog"] = BlogPost.objects.get(slug = self.kwargs["slug"])
        return context
    
    def get(self,request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def post(self,request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)