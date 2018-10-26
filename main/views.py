from django.shortcuts import render
from .models import StaffMember

def index(request):

    # Query all staff members for display on the landing page
    staff = StaffMember.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'main/index.html', context)
