from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView
from django.contrib import messages

from restaurant.models import Category, Dish
from .forms import *


def categories(request):
    items = Category.objects.all().order_by('category_order')
    return render(request, 'categories_view.html', context={'items': items})

class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('menu:categories')
    success_message = 'Категорія успішно відкоригована!'

class CategoryAddView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_add.html'
    success_url = reverse_lazy('menu:categories')
    success_message = 'Категорія успішно створена!'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('menu:categories')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Категорія успішно видалена!')
        return self.post(request, *args, **kwargs)



def dishes(request):
    items = Dish.objects.all()
    return render(request, 'dishes_view.html', context={'items': items})


class DishUpdateView(SuccessMessageMixin, UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_update.html'
    success_url = reverse_lazy('menu:dishes')
    success_message = 'Страва успішно відкоригована!'

class DishAddView(SuccessMessageMixin, CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_add.html'
    success_url = reverse_lazy('menu:dishes')
    success_message = 'Страва успішно створена!'


class DishDeleteView(DeleteView):
    model = Dish
    success_url = reverse_lazy('menu:dishes')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Страва успішно видалена!')
        return self.post(request, *args, **kwargs)

