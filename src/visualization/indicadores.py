from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_indicadores(request):

    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
    else:
        frequency = "monthly"

    # Fetch graph from the API
    response = requests.get(f"{api}graph/indicadores/?time_frame={frequency}")
    indicadores_html = response.json()
    graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 90%; padding-bottom: 20px;'>{indicadores_html}</div>"

    return render(request, "indicadores.html", {"indicadores": graph})
