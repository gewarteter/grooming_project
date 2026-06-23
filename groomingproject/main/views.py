from django.shortcuts import render
from .models import Appointment

def appointment_list(request):
    appointments = Appointment.objects.select_related('client', 'pet', 'master', 'service').all()
    return render(request, 'appointments.html', {'appointments': appointments})