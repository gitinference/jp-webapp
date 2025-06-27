import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]

def web_app_macro(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        column = request.POST.get("columns")
    else:
        frequency = "fiscal"
        column = 'producto_bruto_(millones_$)'

    temp_col = column.lower()
    temp_freq = frequency.lower()
    graph, context = requests.get(f"{API_URL}/graph/macro/?time_frame={temp_freq}&column={temp_col}").json()

    return render(request, "macro.html", 
                    {
                        "graph": graph, 
                        "api": API_URL, 
                        "selected_frequency": frequency, 
                        "selected_column": column, 
                        **context})
