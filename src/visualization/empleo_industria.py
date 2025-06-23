from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def empleo_industria(request):
  

  return render(request, "empleo_industria.html")