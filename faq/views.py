from django.shortcuts import render, get_object_or_404
from .models import Faq
from .forms import FaqForm

# Create your views here.


def all_faq(request):
    """ Get all FAQs """
    faq = Faq.objects.all()
    context = {
        'faq': faq
    }
    return render(request, 'faq/faq.html', context)


def edit_question(request, faq_id):
    """ Edit FAQ """
    question = get_object_or_404(Faq, pk=faq_id)
    form = FaqForm(instance=question)

    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'faq/edit_question.html', context)
