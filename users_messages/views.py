from django.shortcuts import render, redirect
from restaurant.models import UsersMessages

def home(request):
    messages = UsersMessages.objects.filter(is_processed=False).order_by('send_date')
    return render(request, 'messages.html', context={'items': messages})

def update_message(request, pk):
    UsersMessages.objects.filter(pk=pk).update(is_processed=True)
    return redirect('/messages/')