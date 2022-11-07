from django.shortcuts import render



def avtomobil(request):
    return render(request , 'avtomobil.html')

def kompyuter(request):
    return render(request , 'kompyuter.html')

def meva(request):
    return render(request , 'meva.html')

def kitob(request):
    return render(request , 'kitob.html')

def sabzavot(request):
    return render(request , 'sabzavot.html')
def telefon(request):
    return render(request , 'telefon.html')