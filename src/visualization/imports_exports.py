import polars as pl
import plotly.express as px
from django.shortcuts import render
import requests
import pandas as pd
import os
import sys
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def web_app_imports_exports(request):

    # IMPORTS GRAPH 

    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")
        level_filter = request.POST.get("hts_codes")

        if frequency is None and second_dropdown is None:
            frequency = "Yearly"
            second_dropdown = 2024
            level_filter = '0000'
        
        imports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame=yearly&datetime=2009&group=false&frequency={frequency}&second_dropdown={second_dropdown}&third_dropdown={third_dropdown}&type=imports&level_filter={level_filter}"
        )
    else:
        imports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame=yearly&group=false&frequency=Yearly&second_dropdown=2024&datetime=2024&type=imports"
        )

    imports, hts_codes = imports_graph.json()

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # EXPORTS GRAPH

    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        third_dropdown_2 = request.POST.get("third_dropdown_2")
        level_filter_2 = request.POST.get("hts_codes_2")

        if frequency_2 is None and second_dropdown_2 is None:
            frequency_2 = "Yearly"
            second_dropdown_2 = 2024
            level_filter_2 = '0000'

        exports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame=yearly&datetime=2009&group=false&frequency={frequency_2}&second_dropdown={second_dropdown_2}&third_dropdown={third_dropdown_2}&type=exports&level_filter={level_filter_2}"
        )
    else:
        exports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame=yearly&group=false&frequency=Yearly&second_dropdown=2024&datetime=2024&type=exports"
        )

    exports, hts_codes_2 = exports_graph.json()

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    context = {
        "imports": imports,
        "exports": exports,
        "api": api,
        **hts_codes
    }

    return render(request, "imports_exports.html", context)
