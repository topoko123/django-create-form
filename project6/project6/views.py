from django.shortcuts import render
from .forms import *

def index(request):
    return render(request, 'index.html')

def chrfield(request):
    if request.method == 'POST':
        form = ChrFieldForm(request.POST)
    else:
        form = ChrFieldForm()

    return render(request, 'chrfield.html', {'form': form})

def number(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        q = request.POST.get('quantity', 0)
        p = request.POST.get('price', 0)
    else:
        form = NumberForm()
        q = 0
        p = 0

    try:
        total = int(q) * float(p)
    except:
        total = 0
    
    data = {'form': form, 'quantity': q, 'price': p, 'total': total}
    return render(request, 'number.html', data)

def email_url(request):
    if request.method == 'POST':
        form = EmailURLForm(request.POST)
    else:
        form = EmailURLForm()

    return render(request, 'email-url.html', {'form': form})

def boolean(request):
    if request.method == 'POST':
        form = BooleanForm(request.POST)
    else:
        form = BooleanForm()

    return render(request, 'boolean.html', {'form': form})

def choice(request):
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
    else:
        form = ChoiceForm()

    return render(request, 'choice.html', {'form': form})