from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Faq
from .forms import FaqForm
from django.contrib import messages

# Create your views here.


def all_faq(request):
    """ Get all FAQs """
    faq = Faq.objects.all()
    context = {
        'faq': faq
    }
    return render(request, 'faq/faq.html', context)


def add_question(request):
    """ Add question into FAQ """
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added question!')
            return redirect('all_faq')
        else:
            messages.error(request, 'Failed to add question. Please ensure the form is valid.')
    else:
        form = FaqForm()

    template = 'faq/add_question.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_question(request, faq_id):
    """ Edit question in FAQ """
    question = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated question!')
            return redirect('all_faq')
        else:
            messages.error(request, 'Failed to update question. Please ensure the form is valid.')
    else:
        form = FaqForm(instance=question)
        messages.info(request, f'You are editing question: "{question.question}"')

    template = 'faq/edit_question.html'
    context = {
        'form': form,
        'question': question,
    }
    return render(request, template, context)
