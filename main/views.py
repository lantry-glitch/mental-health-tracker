from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152134',
        'name': 'Allan Kwek',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

# Create your views here.
