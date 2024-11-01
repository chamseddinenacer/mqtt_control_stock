from django.shortcuts import render
from django.utils import timezone
from .mqtt_client import start_mqtt, stop_mqtt   

piece = {
    'count': 0,
    'start_date': None,
    'end_date': None,
    'running': False,
    'activation_dates': []
}

def control_view(request):
    global piece

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "start" and not piece['running']:
            piece['start_date'] = timezone.now()
            piece['running'] = True
            piece['count'] += 1
            piece['end_date'] = None
            piece['activation_dates'].append(piece['start_date'])
            start_mqtt()   
        elif action == "stop" and piece['running']:
            piece['end_date'] = timezone.now()
            piece['running'] = False
            stop_mqtt()  

    context = {'piece_name': "piece_1", 'piece_info': piece}
    return render(request, 'control.html', context)
def dashboard(request):
    return render(request, 'dashboard.html')