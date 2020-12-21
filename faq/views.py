from django.shortcuts import render
from faq.models import Faq

# Create your views here.


def Faq(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq
    }
    return render(request, 'faq/faq.html', context)

