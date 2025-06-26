from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_proyecciones(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
        column = request.POST.get("columns")
    else:
        frequency = request.GET.get("frequency", "yearly").lower()
        column = request.GET.get("columns", 'componentes')

    response = requests.get(f"{api}graph/proyecciones/?time_frame={frequency}&column={column}")
    proyecciones_html, columns = response.json()

    return render(request, "proyecciones.html", {"graph": proyecciones_html, **columns, 'selected_frequency': frequency, 'selected_column': column, "api" : api,})