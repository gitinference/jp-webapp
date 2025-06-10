import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def indice_consumidor(request):
    # URLs for each frequency
    response = requests.get(f"{API_URL}/graph/product-ranking")
    graphs = response.json()

    # Validate required columns
    return render(request, "indice_consumidor.html")

