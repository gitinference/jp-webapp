from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_num_neg_industria(request):
    if request.method == "POST":
      frequency = request.POST.get("frequency").lower()
      column = request.POST.get("columns")
    else:
      frequency = "yearly"
      column = '(N1111) Oilseed and Grain Farming'

    # Fetch graph from the API
    response = requests.get(f"{api}graph/nomina/?time_frame={frequency}&data_type=nivel&naics_desc={column}&column=businesses").json()
    empleo_html, context = response

    return render(request, "num_negocios_sector_ind.html", 
            {
                "graph": empleo_html, 
                "api": api, 
                **context, 
                "selected_frequency": frequency, 
                "selected_column": column,
            })