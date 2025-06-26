from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_ciclos_economicos(request):

    if request.method == "POST":
        column = request.POST.get("columns")
    else:
        column = request.GET.get("columns", 'encuesta_de_establecimientos')

    # Fetch graph from the API
    response = requests.get(f"{api}graph/jp/cycles/?column={column}")
    ciclos_economicos_html, columns = response.json()

    return render(request, "ciclos_economicos.html", {"ciclos_economicos": ciclos_economicos_html, "api": api, "selected_column": column, **columns})