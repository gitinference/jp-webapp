import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def productos_ranking(request):
    # URLs for each frequency
    response = requests.get(f"{API_URL}/graph/product-ranking")
    graphs = response.json()

    export_top = graphs.get("export_top")
    export_bottom = graphs.get("export_bottom")
    import_top = graphs.get("import_top")
    import_bottom = graphs.get("import_bottom")

    context = {
        "graph_export_top": export_top,
        "graph_export_bottom": export_bottom,
        "graph_import_top": import_top,
        "graph_import_bottom": import_bottom,
        "api": API_URL
    }

    # Validate required columns
    return render(
        request,
        "productos_ranking.html",
        context
    )

