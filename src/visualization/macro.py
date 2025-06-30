import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]

def web_app_macro(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        column = request.POST.get("columns")
        frequency_2 = request.POST.get("frequency_2")
        column_2 = request.POST.get("columns_2")
    else:
        frequency = "fiscal"
        column = 'producto_bruto_(millones_$)'
        frequency_2 = "fiscal"
        column_2 = 'producto_bruto_(millones_$)'

    temp_col = column.lower()
    temp_freq = frequency.lower()
    temp_col_2 = column_2.lower()
    temp_freq_2 = frequency_2.lower()
    graph, context = requests.get(f"{API_URL}/graph/macro/?time_frame={temp_freq}&column={temp_col}&data_type=df_1950").json()

    graph_2, context_2 = requests.get(f"{API_URL}/graph/macro/?time_frame={temp_freq_2}&column={temp_col_2}&data_type=df_2001").json()

    return render(request, "macro.html", 
                    {
                        "graph": graph, 
                        "graph2001": graph_2,
                        "api": API_URL, 
                        "selected_frequency": frequency, 
                        "selected_column": column, 
                        "selected_frequency_2": frequency_2, 
                        "selected_column_2": column_2, 
                        **context,
                        **context_2})
