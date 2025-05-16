import polars as pl
import plotly.express as px
from django.shortcuts import render
from dotenv import load_dotenv
import requests
import pandas as pd
import os
import sys

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Now import from env
from env import get_db_credentials


load_dotenv()

creds = get_db_credentials()
api = creds[6]

print(api)
def web_app_imports_exports(request):

    df1_imports = requests.get(f"{api}data/trade/jp/?time_frame=yearly&level=country&agg=none&agr=false&group=false&datetime=2009").json()
    df1_imports = pd.DataFrame(df1_imports)

    # IMPORTS GRAPH 
    fig = px.pie(df1_imports, values='imports', names='country')
    fig.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        frequency = request.POST.get("frequency")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")

        if frequency == "Yearly":
            df1_imports = requests.get(f"{api}data/trade/jp/?time_frame=yearly&level=country&agg=none&agr=false&group=false&datetime={second_dropdown}").json()
            fig = px.pie(df1_imports, values='imports', names='country')
        elif frequency == "Monthly":
            df1_imports = requests.get(f"{api}data/trade/jp/?time_frame=monthly&level=country&agg=none&agr=false&group=false&datetime={second_dropdown}-{third_dropdown}").json()
            fig = px.pie(df1_imports, values='imports', names='country')
        elif frequency == "Quarterly":
            df1_imports = requests.get(f"{api}data/trade/jp/?time_frame=qrt&level=country&agg=none&agr=false&group=false&datetime={second_dropdown}-{third_dropdown}").json()
            fig = px.pie(df1_imports, values='imports', names='country')

        if frequency is None and second_dropdown is None:
            frequency = "Yearly"
            second_dropdown = 2009

        if third_dropdown is None:
            fig.update_layout(
                title={
                    'text': f"Time: {frequency} / {second_dropdown}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )
        else:
            fig.update_layout(
                title={
                    'text': f"Time: {frequency} / {second_dropdown} / {third_dropdown}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )

    fig.update_traces(textposition='inside', textinfo='percent+label')

    imports = fig.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    # EXPORTS GRAPH
    
    df1_exports = requests.get(f"{api}data/trade/jp/?time_frame=yearly&level=country&agg=none&agr=false&group=false&datetime=2009").json()
    df1_exports = pd.DataFrame(df1_exports)
    
    fig1 = px.pie(df1_exports, values='exports', names='country')
    fig1.update_traces(textposition='inside', textinfo='percent+label')

    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        second_dropdown_2 = request.POST.get("second_dropdown_2")
        third_dropdown_2 = request.POST.get("third_dropdown_2")

        if frequency_2 == "Yearly":
            df1_exports = requests.get(f"{api}data/trade/jp/?time_frame=yearly&level=country&agg=none&agr=false&group=false&datetime={second_dropdown_2}").json()
            fig1 = px.pie(df1_exports, values='exports', names='country')
        elif frequency_2 == "Monthly":
            df1_exports = requests.get(f"{api}data/trade/jp/?time_frame=monthly&level=country&agg=none&agr=false&group=false&datetime={second_dropdown_2}-{third_dropdown_2}").json()
            fig1 = px.pie(df1_exports, values='exports', names='country')
        elif frequency_2 == "Quarterly":
            df1_exports = requests.get(f"{api}data/trade/jp/?time_frame=qrt&level=country&agg=none&agr=false&group=false&datetime={second_dropdown_2}-{third_dropdown_2}").json()
            fig1 = px.pie(df1_exports, values='exports', names='country')

        if frequency_2 is None and second_dropdown_2 is None:
            frequency_2 = "Yearly"
            second_dropdown_2 = 2009

        if third_dropdown_2 is None:
            fig1.update_layout(
                title={
                    'text': f"Time: {frequency_2} / {second_dropdown_2}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )
        else:
            fig1.update_layout(
                title={
                    'text': f"Time: {frequency_2} / {second_dropdown_2} / {third_dropdown_2}",
                    'x': 0.5,
                    'font': {'color': 'black'}
                },
            )

    fig1.update_traces(textposition='inside', textinfo='percent+label')

    exports = fig1.to_html(full_html=False, default_height=500, default_width=700)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------

    context = {
        "imports": imports,
        "exports": exports
    }

    return render(request, "imports_exports.html", context)
