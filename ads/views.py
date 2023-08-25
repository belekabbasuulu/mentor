from typing import Any, Dict
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.utils import timezone
import datetime
from django.urls import reverse, reverse_lazy
from users.models import User
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Ads, Category
from .forms import AdForm


def category_list(request):
    all_categories = Category.objects.all()
    context = {
        "all_categories": all_categories
    }
    return render(request, 'category.html', context=context)


class AdsListView(ListView):
    template_name = 'index.html'
    queryset = Ads.objects.all()
    context_object_name = 'all_ads'


class AdsDetailView(DetailView):
    template_name = 'retrieve_ad.html'
    queryset = Ads.objects.all()
    context_object_name = 'ad'


class AdsDeleteView(DeleteView):
    queryset = Ads.objects.all()
    template_name = 'delete_ad.html'
    success_url = reverse_lazy('ads-list')


class AdsUpdateView(UpdateView):
    template_name = 'update_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads-list')


class AdsCreateView(CreateView):
    template_name = 'create_ad.html'
    queryset = Ads.objects.all()
    form_class = AdForm

    def get_success_url(self):
        return reverse('ads-list')

    # def get(self, request, *args, **kwargs):
    #     all_ads = Ads.objects.all()
    #     return render(request, self.template_name, {'all_ads': all_ads})

    # all_ads = Ads.objects.filter(created_at__lte=timezone.now())
    # all_ads = Ads.objects.filter(title__icontains='test')
    # all_ads = Ads.objects.filter(owner__isnull=True)
    # all_ads = Ads.objects.filter(description__icontains='s').filter(created_at__year=2023)
    # admin = User.objects.get(username='admin')
    # all_ads = Ads.objects.filter(owner=admin)
    # all_ads = Ads.objects.filter(price__in=[200, 3000, 343, 2500])

    # 1 - azyrkyga cheyinki ads chygargyla
    # 2 - title ichinde "test" degen soz bolso chygargyla
    # 3 - owner joktordu chygargyla
    # 4 - 2023 chykkan jana descriptionda "b" chygargyla
    # 5 - owner == "admin" chygargyla
    # 6 - price --> [200, 3000, 343, 2500] ichinde bolso chygargyla


    # ad = Ads.objects.get(price=150)
    # all_ads = Ads.objects.filter(title__iexact="TesT upDate")
    # all_ads = Ads.objects.filter(title__contains="Test")
    # all_ads = Ads.objects.filter(price__in=[3000, 343, 500, 900])
    # all_ads = Ads.objects.filter(price__in=[3000, 343, 500, 900])


def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ads-list')
    else:
        form_of_ad = AdForm()
    return render(request, 'create_ad.html', {'form_of_ad': form_of_ad})


def update_ad(request, pk):
    ad = get_object_or_404(Ads, id=pk)

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Success edited </h1>')
        else:
            return HttpResponse('<h1> Error edited </h1>')
    else:
        form_of_ad = AdForm(instance=ad)
        return render(request, 'update_ad.html', {'form_of_ad': form_of_ad})


# def retrieve_ad(request, pk):
#     ad = Ads.objects.get(id=pk)
#     context = {
#         "ad": ad
#     }
#     return render(request, 'retrieve_ad.html', context=context)


def delete_ad(request, pk):
    ad = Ads.objects.get(id=pk)
    ad.delete()
    messages.success(request, 'Объект успешно удален.')
    return redirect('ads-list')




    # if request.method == 'POST':
    #     subcategory_id = request.POST['subcategory']
    #     title = request.POST['title']
    #     description = request.POST['description']
    #     price = request.POST['price']
    #     image = request.FILES.get('image', None)  # Обработка изображения
    #     owner = request.user
    #     type = request.POST['type']

    #     subcategory = SubCategory.objects.get(pk=subcategory_id)

    #     ad = Ads(subcategory=subcategory, title=title, description=description,
    #              price=price, image=image, owner=owner, type=type)
    #     ad.save()

    #     return redirect('index')