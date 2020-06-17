from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(reqest):
    name = "Glen"
    current_day = "03.06.2020"
    form = SubscriberForm(reqest.POST or None)

    if reqest.method == "POST" and form.is_valid():
        print(reqest.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(reqest, 'landing/landing.html', locals())


def home(reqest):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_zakuska = products_images.filter(product__category__name="Закуски")
    products_images_sweets = products_images.filter(product__category__name="Десерты")
    products_images_hot = products_images.filter(product__category__name="Горячие блюда")
    return render(reqest, 'landing/home.html', locals())

