from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_demographic(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
        column = request.POST.get("columns")
    else:
        frequency = request.GET.get("frequency", "yearly").lower()
        column = request.GET.get("columns", 'cambio_natural')

    response = requests.get(f"{api}graph/demographic/?time_frame={frequency}&column={column}")
    demographic_html, columns = response.json()

    return render(request, "demograficos.html", {"graph": demographic_html, **columns, 'selected_frequency': frequency, 'selected_column': column, "api" : api,})