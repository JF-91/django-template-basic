from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def buttons(request):
    return render(request, 'components/buttons.html')

def cards(request):
    return render(request, 'components/cards.html') 