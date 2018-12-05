from django.shortcuts import render
from django.db.models import Q
from .models import StaffMember

def index(request):

    # Retrieve doctors from database and assign to list
    doctors = []
    doctors.append(StaffMember.objects.get(name_key='dantescala'))
    doctors.append(StaffMember.objects.get(name_key='josephscala'))

    # Retrieve staff from database (without doctors) and assign to list
    staff = StaffMember.objects.exclude(
        Q(name_key='dantescala') | Q(name_key='josephscala')
    ).order_by('name')

    context = {
        'doctors': doctors,
        'staff': staff,
    }

    return render(request, 'main/index-v1.html', context)