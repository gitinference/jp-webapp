import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()
api = creds[6]

def gastos_gobierno_estatal(request):
    # Default values
    period_gasto = request.GET.get("period_gasto", "monthly").lower()
    metric_gasto = request.GET.get("metric_gasto", "contrib_prop_inmueble_ano_corr_e1110")

    period_revenue = request.GET.get("period_revenue", "monthly").lower()
    metric_revenue = request.GET.get("metric_revenue", "contrib_prop_inmueble_ano_corr_r0110")

    if request.method == "POST":
        period_gasto = request.POST.get("period_gasto", period_gasto).lower()
        metric_gasto = request.POST.get("metric_gasto", metric_gasto)

        period_revenue = request.POST.get("period_revenue", period_revenue).lower()
        metric_revenue = request.POST.get("metric_revenue", metric_revenue)

    # Request gastos (expenditures) graph
    response_gasto = requests.get(
        f"{api}/graph/jp/gastos_estatales/",
        params={"period": period_gasto, "metric": metric_gasto}
    )
    response_gasto.raise_for_status()
    gasto_html, gasto_dict = response_gasto.json()

    # Request revenue graph
    response_revenue = requests.get(
        f"{api}/graph/jp/revenues_estatales/",
        params={"period": period_revenue, "metric": metric_revenue}
    )
    response_revenue.raise_for_status()
    revenue_html, revenue_dict = response_revenue.json()



    # Render both graphs in same page
    context = {
        "gasto_graph": f"<div style='overflow-x: auto; white-space: nowrap; width: 100%; padding-bottom: 20px;'>{gasto_html}</div>",
        "revenue_graph": f"<div style='overflow-x: auto; white-space: nowrap; width: 100%; padding-bottom: 20px;'>{revenue_html}</div>",
        "api": api,
        "period_gasto": period_gasto,
        "metric_gasto": metric_gasto,
        "period_revenue": period_revenue,
        "metric_revenue": metric_revenue,
        **gasto_dict,
        **revenue_dict,
    }

    return render(request, "gastos_gobierno_estatal.html", context)
