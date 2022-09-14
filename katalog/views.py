# TODO: Create your views here.
from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):

    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Aghniya Zhafira',
        'npm': '2106654164'
    }
    return render(request,"katalog.html", context)