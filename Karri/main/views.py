from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def kontaktu(request):
    return render(request, 'main/kontaktu.html')


def onas(request):
    return render(request, 'main/onas.html')
