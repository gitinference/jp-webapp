import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def gastos_gobierno_estatal(request):
    # 1) pull the user’s inputs (POST or GET)
    if request.method == "POST":
        period = request.POST.get("period", "").lower()
        metric = request.POST.get("metric", "")
    else:
        period = request.GET.get("period", "monthly").lower()
        metric = request.GET.get("metric", "contrib_prop_inmueble_ano_corr_r0110")

    url = f"{api}/graph/jp/estatales/"
    params = {"period": period, "metric": metric}
    response = requests.get(url, params=params)
    response.raise_for_status()

    gastos_html, metrics_dict = response.json()

    context = {
        "graph": gastos_html,
        "api": api,
        "period": period,
        "metric": metric,
        **metrics_dict, 
    }
    return render(request, "gastos_gobierno_estatal.html", context)
