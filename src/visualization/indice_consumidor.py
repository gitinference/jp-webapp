import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def web_app_indice_consumidor(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
    else:
        frequency = "yearly"

    # Fetch graph from the API
    response = requests.get(f"{API_URL}graph/consumer/?time_frame={frequency}")
    indice_consumidor_html = response.json()
    graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 90%; padding-bottom: 20px;'>{indice_consumidor_html}</div>"

    return render(request, "indice_consumidor.html", {"consumer": graph, "api": API_URL})

