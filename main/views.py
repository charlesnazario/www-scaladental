from django.shortcuts import render
from .models import StaffMember

def index(request):

    context = {}
    return render(request, 'main/index.html', context)

def ouroffice(request):

    staff = StaffMember.objects.all()
    context = {
        'staff': staff,
    }

    return render(request, 'main/ouroffice.html', context)

def contact(request):
    context = {}
    return render(request, 'main/contact.html', context)