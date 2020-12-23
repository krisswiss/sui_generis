from django.shortcuts import render
from .models import Faq

# Create your views here.


def all_faq(request):
    faq = Faq.objects.all()
    context = {
        'faq': faq
    }
    return render(request, 'faq/faq.html', context)


def edit_faq(request, pk):
    question = Faq.objects.get(pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'faq/edit_faq.html', context)