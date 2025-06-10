from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_income_employment(request):
  
  naics = None
  
  if request.method == "POST":
    naics_time = request.POST.get("naics_time")
  else:
    naics_time = "1111"
    
  response = requests.get(f"{api}graph/naics/?naics_code={naics_time}")
  graph, naics = response.json()
    
  html_graph = f'<div style="padding-left: 120px;">{graph}</div>'

  return render(request, "income_employment.html", {'graph': html_graph, **naics})