import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]

def gastos_gobierno_federal(request):

    return render(request, "gastos_gobierno_federal.html")

