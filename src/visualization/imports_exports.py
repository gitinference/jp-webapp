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
            frequency = "yearly"
            second_dropdown = 2024
            level_filter = '0101'
        
        imports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame={frequency}&datetime={second_dropdown}&group=false&frequency={frequency}&second_dropdown={second_dropdown}&third_dropdown={third_dropdown}&type=imports&level_filter={level_filter}"
        )
    else:
        frequency = "yearly"
        second_dropdown = 2024
        third_dropdown = 1
        level_filter = '0101'
        imports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame={frequency}&group=false&frequency={frequency}&second_dropdown={second_dropdown}&datetime={second_dropdown}&type=imports"
        )

    imports, hts_codes = imports_graph.json()

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # EXPORTS GRAPH

    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        third_dropdown_2 = request.POST.get("third_dropdown_2")
        level_filter_2 = request.POST.get("hts_codes_2")
        print(second_dropdown_2, third_dropdown_2)

        if frequency_2 is None and second_dropdown_2 is None:
            frequency_2 = "Yearly"
            second_dropdown_2 = 2024
            level_filter_2 = '0101'

        exports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame=yearly&datetime=2009&group=false&frequency={frequency_2}&second_dropdown={second_dropdown_2}&third_dropdown={third_dropdown_2}&type=exports&level_filter={level_filter_2}"
        )
    else:
        frequency_2 = "yearly"
        second_dropdown_2 = 2024
        third_dropdown_2 = 1
        level_filter_2 = '0101'
        exports_graph = requests.get(
            f"{api}graph/import-export/?level=country&time_frame={frequency_2}&group=false&frequency={frequency_2}&second_dropdown={second_dropdown_2}&datetime={second_dropdown_2}&type=exports"
        )

    exports, hts_codes_2 = exports_graph.json()

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    context = {
        "imports": imports,
        "exports": exports,
        "api": api,
        **hts_codes,
        "selected_frequency": frequency,
        "selected_second_dropdown": second_dropdown,
        "selected_third_dropdown": third_dropdown,
        "selected_level_filter": level_filter,
        "selected_frequency_2": frequency_2,
        "selected_second_dropdown_2": second_dropdown_2,
        "selected_third_dropdown_2": third_dropdown_2,
        "selected_level_filter_2": level_filter_2,
    }

    return render(request, "imports_exports.html", context)
