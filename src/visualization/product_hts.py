import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]

def products_hts(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        hts_code = request.POST.get("hts_code")
        trade_type = request.POST.get("trade_type")
        frequency_2 = request.POST.get("frequency_2")
        hts_code_2 = request.POST.get("hts_code_2")
        trade_type_2 = request.POST.get("trade_type_2")
        frequency_3 = request.POST.get("frequency_3")
        hts_code_3 = request.POST.get("hts_code_3")
        trade_type_3 = request.POST.get("trade_type_3")
    else:
        frequency = "yearly"
        hts_code = "0101"
        trade_type = "imports"
        frequency_2 = "yearly"
        hts_code_2 = "0101"
        trade_type_2 = "imports"
        frequency_3 = "yearly"
        hts_code_3 = "0101"
        trade_type_3 = "imports"

    print(
        f"Frequency: {frequency} | HTS Code: {hts_code} | Trade Type: {trade_type}"
    )

    graph, context = requests.get(f"{API_URL}/graph/product-hts/?level=hts&time_frame={frequency}&agriculture_filter=false&group=false&level_filter={hts_code}&trade_type={trade_type}&data_type=nivel").json()

    pd_graph, context = requests.get(f"{API_URL}/graph/product-hts/?level=hts&time_frame={frequency_2}&agriculture_filter=false&group=false&level_filter={hts_code_2}&trade_type={trade_type_2}&data_type=primera_diferencia").json()

    cp_graph, context = requests.get(f"{API_URL}/graph/product-hts/?level=hts&time_frame={frequency_3}&agriculture_filter=false&group=false&level_filter={hts_code_3}&trade_type={trade_type_3}&data_type=cambio_porcentual").json()

    return render(request, "product_hts.html", 
                  {
                      "graph": graph, 
                      "pd_graph": pd_graph, 
                      "cp_graph": cp_graph, 
                      "api": API_URL, 
                      "selected_frequency": frequency, 
                      "selected_hts_code": hts_code, 
                      "selected_trade_type": trade_type,
                      "selected_frequency_2": frequency_2, 
                      "selected_hts_code_2": hts_code_2, 
                      "selected_trade_type_2": trade_type_2,
                      "selected_frequency_3": frequency_3, 
                      "selected_hts_code_3": hts_code_3, 
                      "selected_trade_type_3": trade_type_3,
                        **context})

