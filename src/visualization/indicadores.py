from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_indicadores(request):

    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
        frequency_2 = request.POST.get("frequency_2").lower()
        frequency_3 = request.POST.get("frequency_3").lower()
        column = request.POST.get("columns")
        column_2 = request.POST.get("columns_2")
        column_3 = request.POST.get("columns_3")
    else:
        frequency = request.GET.get("frequency", "yearly").lower()
        frequency_2 = request.GET.get("frequency_2", "yearly").lower()
        frequency_3 = request.GET.get("frequency_3", "yearly").lower()
        column = request.GET.get("columns", 'encuesta_de_establecimientos')
        column_2 = request.GET.get("columns_2", 'encuesta_de_establecimientos')
        column_3 = request.GET.get("columns_3", 'encuesta_de_establecimientos')

    # Fetch graph from the API
    response = requests.get(f"{api}graph/indicadores/?time_frame={frequency}&column={column}&data_type=indices_precio")
    indicadores_html, columns = response.json()
    graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 90%; padding-bottom: 20px;'>{indicadores_html}</div>"

    response = requests.get(f"{api}graph/indicadores/?time_frame={frequency_3}&column={column_3}&data_type=primera_diferencia")
    primera_diferencia, columns = response.json()
    primera_diferencia_graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 90%; padding-bottom: 20px;'>{primera_diferencia}</div>"

    response = requests.get(f"{api}graph/indicadores/?time_frame={frequency_2}&column={column_2}&data_type=cambio_porcentual")
    cambio_porcentual, columns = response.json()
    cambio_porcentual_graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 90%; padding-bottom: 20px;'>{cambio_porcentual}</div>"

    return render(request, "indicadores.html", 
                  {
                      "indicadores": graph,
                      "primera_diferencia": primera_diferencia_graph,
                      "cambio_porcentual": cambio_porcentual_graph, 
                      "api": api, 
                      "selected_frequency": frequency, 
                      "selected_frequency_2": frequency_2,
                      "selected_frequency_3": frequency_3,
                      "column_post": column,
                      "column_post_2": column_2,
                      "column_post_3": column_3,
                      **columns})
