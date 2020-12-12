from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ Bag view """

    return render(request, 'bag/bag.html')
