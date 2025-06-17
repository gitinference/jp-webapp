import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def web_app_indice_consumidor(request):

    # Indices Consumidor
    #-----------------------------------------------------------------#
    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
    else:
        frequency = "yearly"

    # Fetch graph from the API
    response = requests.get(f"{API_URL}graph/consumer/?time_frame={frequency}")
    indice_consumidor_html = response.json()
    graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 90%; padding-bottom: 20px;'>{indice_consumidor_html}</div>"

    # Indices Precios
    #-----------------------------------------------------------------#
    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2").lower()
        data_type = request.POST.get("data_type")
        column_2 = request.POST.get("columns_2")
    else:
        frequency_2 = "yearly"
        data_type = 'indices_precio'
        column_2 = 'hts_1_deflated'


    response = requests.get(f"{API_URL}graph/indices/precios/?time_frame={frequency_2}&data_type={data_type}&column={column_2}")
    indice_precios_html, precios = response.json()

    return render(request, "indice_consumidor.html", {"consumer": graph, "api": API_URL, "indices_precios": indice_precios_html, **precios,})

