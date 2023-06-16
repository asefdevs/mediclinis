from core.models import Settings,Appointment,Doctors,Comment

def settings(request):
    context={
        "settings":Settings.objects.first(),
    }
    return context

def counter(request):
    context={
        'appointment_count': Appointment.objects.count(),
        'doctor_count': Doctors.objects.count(),
    }
    return context

def comments(request):
    context={
        'comments':Comment.objects.all().order_by('-created_at'),
    }
    return context
