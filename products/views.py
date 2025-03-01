from django.shortcuts import render

from .models import Category, Advertisement, User
from django.views.generic import ListView, CreateView, DetailView

# Create your views here.


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'


class AdvertisementCreateView(CreateView):
    model = Advertisement
    template_name = 'announce.html'


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'main.html'
    context_object_name = 'advertisements'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            return Advertisement.objects.filter(category_id=category_id)
        return Advertisement.objects.all()

class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'single.html'
    pk_url_kwarg = 'id'



def login(request):
    return render(request, 'login.html')


class UserProfileCreateView(CreateView):
    model = User
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class AdvertisementSearchView(ListView):
    model = Advertisement
    template_name = "search_results.html"
    context_object_name = "advertisements"
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()
        if query:
            return Advertisement.objects.filter(title__icontains=query).order_by('-created_at')
        return Advertisement.objects.none()
