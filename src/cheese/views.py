from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Fromage


def home(request):
    return render(request, 'cheese/home.html')


def allcheese(request):
    fromages = Fromage.objects.all()
    return render(request, 'cheese/allcheese.html', context={'fromages': fromages})


def patepresseescuite(request):
    fromages = Fromage.objects.filter(category="PPC")
    return render(request, 'cheese/patepresseescuite.html', context={'fromages': fromages})


def patemolle(request):
    fromages = Fromage.objects.filter(category="PMO")
    return render(request, 'cheese/patemolle.html', context={'fromages': fromages})


def patefleurie(request):
    fromages = Fromage.objects.filter(category="PFL")
    return render(request, 'cheese/patefleurie.html', context={'fromages': fromages})


def fromagedechevre(request):
    fromages = Fromage.objects.filter(category="FCH")
    return render(request, 'cheese/fromagedechevre.html', context={'fromages': fromages})


def fromagedebrebis(request):
    fromages = Fromage.objects.filter(category="FBR")
    return render(request, 'cheese/fromagedebrebis.html', context={'fromages': fromages})


def patepersillee(request):
    fromages = Fromage.objects.filter(category="PPE")
    return render(request, 'cheese/patepersillee.html', context={'fromages': fromages})


def triplecreme(request):
    fromages = Fromage.objects.filter(category="TCR")
    return render(request, 'cheese/triplecreme.html', context={'fromages': fromages})


def pateforte(request):
    fromages = Fromage.objects.filter(category="PFO")
    return render(request, 'cheese/pateforte.html', context={'fromages': fromages})


def product_detail(request, slug):
    fromage = get_object_or_404(Fromage, slug=slug)
    return render(request, 'cheese/detail.html', context={"fromage": fromage})


def contact(request):
    return render(request, 'cheese/contact.html')


def lieux(request):
    return render(request, 'cheese/lieux.html')


def recettes(request):
    return render(request, 'cheese/recettes.html')


def questions(request):
    return render(request, 'cheese/questions.html')


def livraison(request):
    return render(request, 'cheese/livraison.html')


def nous(request):
    return render(request, 'cheese/nous.html')


def origine_nord(request):
    fromages = Fromage.objects.filter(origin="du Nord de la France")
    return render(request, 'cheese/origine_nord.html', context={'fromages': fromages})


def plateau(request):
    return render(request, 'cheese/plateau.html')
