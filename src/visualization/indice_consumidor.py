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
        frequency_2 = request.POST.get("frequency_2").lower()
        frequency_3 = request.POST.get("frequency_3").lower()
        column = request.POST.get("columns")
        column_2 = request.POST.get("columns_2")
        column_3 = request.POST.get("columns_3")
    else:
        frequency = "yearly"
        frequency_2 = "yearly"
        frequency_3 = "yearly"
        column = 'agua_alcantarillados_y_limpieza_de_pozos_septicos'
        column_2 = 'agua_alcantarillados_y_limpieza_de_pozos_septicos'
        column_3 = 'agua_alcantarillados_y_limpieza_de_pozos_septicos'

    # Fetch graph from the API
    response = requests.get(f"{API_URL}graph/consumer/?time_frame={frequency}&data_type=indices_precio&column={column}").json()
    indice_consumidor_html, context = response

    response = requests.get(f"{API_URL}graph/consumer/?time_frame={frequency_2}&data_type=cambio_porcentual&column={column_2}").json()
    cambio_porcentual_html, context = response

    response = requests.get(f"{API_URL}graph/consumer/?time_frame={frequency_3}&data_type=primera_diferencia&column={column_3}").json()
    primera_diferencia_html, context = response

    return render(request, "indice_consumidor.html", 
            {
                "consumer": indice_consumidor_html, 
                "api": API_URL, 
                "cambio_porcentual": cambio_porcentual_html, 
                "primera_diferencia": primera_diferencia_html, 
                **context, 
                "selected_frequency": frequency, 
                "selected_frequency_2": frequency_2,
                "selected_frequency_3": frequency_3,
                "selected_column": column,
                "selected_column_2": column_2,
                "selected_column_3": column_3
            })

