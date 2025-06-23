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
    else:
        frequency = "yearly"
        hts_code = "0101"
        trade_type = "imports"

    print(
        f"Frequency: {frequency} | HTS Code: {hts_code} | Trade Type: {trade_type}"
    )

    graph, context = requests.get(f"{API_URL}/graph/product-hts/?level=hts&time_frame={frequency}&agriculture_filter=false&group=false&level_filter={hts_code}&trade_type={trade_type}").json()
    html_graph = f'<div style="padding-left: 120px;">{graph}</div>'

    return render(request, "product_hts.html", {"graph": html_graph, "api": API_URL, "selected_frequency": frequency, "selected_hts_code": hts_code, "selected_trade_type": trade_type, **context})

