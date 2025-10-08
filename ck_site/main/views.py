from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Signup


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def events(request):
    items = Event.objects.all()
    return render(request, 'main/events.html', { 'events': items })


def signup(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        if not name or not email:
            messages.error(request, 'Name and email are required.')
        else:
            Signup.objects.create(event=event, name=name, email=email, phone=phone)
            messages.success(request, 'Thank you! You are signed up.')
            return redirect('events')
    return render(request, 'main/signup.html', { 'event': event })


def donate(request):
    return render(request, 'main/donate.html')


def contact(request):
    if request.method == 'POST':
        # For now, just show a success message
        messages.success(request, 'Thanks! We received your message.')
        return redirect('contact')
    return render(request, 'main/contact.html')
