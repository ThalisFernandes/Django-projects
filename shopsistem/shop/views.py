from django.shortcuts import render,HttpResponse
from shop.models import *

# Create your views here.


def index(request):
    data =  {"nome":"Sorveteria mil grau","endereco":"rua treze de maio nº 100", "contato": "81 998994564","logo":""}
    print(data)
    return render(request, 'main.html',data)