# src/visualization/energy.py

import logging
from django.shortcuts import render
import requests
from env import get_db_credentials

logger = logging.getLogger(__name__)
creds = get_db_credentials()
api = creds[6]

def energy_data(request):
    if request.method == "POST":
        period = request.POST.get("period", "").lower()
        metric = request.POST.get("metric", "")
    else:
        period = request.GET.get("period", "monthly").lower()
        metric = request.GET.get("metric", "generacion_neta_mkwh")

    url = f"{api}graph/energia/?period={period}&metric={metric}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error al llamar a {url}: {e}")
        context = {
            "energia_graph": "",
            "error": f"No pude obtener la gráfica de energía ({e})",
            "period": period,
            "metric": metric,
        }
        return render(request, "energy_data.html", context)
    
    try:
        energy_html, energy_metrics = response.json()
    except ValueError:
        logger.error(
            "JSONDecodeError en respuesta de energía. "
            f"Status: {response.status_code}, Body: {response.text!r}"
        )
        context = {
            "energia_graph": "",
            "error": "La API de energía devolvió un formato inesperado.",
            "period": period,
            "metric": metric,
        }
        return render(request, "energy_data.html", context)

    graph = f"""
    <div style="
      overflow-x: auto;
      white-space: nowrap;
      width: 90%;
      padding-bottom: 20px;
    ">
      {energy_html}
    </div>
    """

    context = {
        "energia_graph": graph,
        "period": period,
        "metric": metric,
        "energy_metrics": energy_metrics,
    }
    return render(request, "energy_data.html", {
    "graph": graph,
    **energy_metrics
})
