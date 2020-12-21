from django.shortcuts import render
from .models import Faq

# Create your views here.


def all_faq(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq
    }
    return render(request, 'faq/faq.html', context)

