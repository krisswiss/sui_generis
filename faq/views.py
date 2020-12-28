from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Faq
from .forms import FaqForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def all_faq(request):
    """ Get all FAQs """
    faq = Faq.objects.all()
    context = {
        'faq': faq
    }
    return render(request, 'faq/faq.html', context)


@login_required
def add_question(request):
    """ Add question into FAQ """
    if not request.user.is_staff or not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def edit_question(request, faq_id):
    """ Edit question in FAQ """
    if not request.user.is_staff or not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_question(request, faq_id):
    """ Delete a question in FAQ """
    if not request.user.is_staff or not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    question = get_object_or_404(Faq, pk=faq_id)
    question.delete()
    messages.success(request, 'Question deleted!')
    return redirect('all_faq')
