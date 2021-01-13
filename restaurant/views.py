from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def main_info(request):

    if request.method == 'POST':
        form = UserMessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    title = 'Gusto'
    phone = '(099) 00-00-001'
    form_user_message = UserMessagesForm()
    categories = Category.objects.filter(is_visible=True)
    for item in categories:
        dishes = Dish.objects.filter(category=item.pk)
        item.dishes = dishes

    special_menu = Dish.objects.filter(category__title='Від шефа')

    return render(request, 'index.html',
                  context={
                      'title': title,
                      'phone': phone,
                      'categories': categories,
                      'special_menu': special_menu,
                      'form': form_user_message,
                  })