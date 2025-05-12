import plotly.graph_objects as go
import pandas as pd
import requests
from django.shortcuts import render
from env import get_db_credentials

API_URL = get_db_credentials()[6]


def productos_ranking(request):
    # URLs for each frequency
    response = requests.get(f"{API_URL}/data/trade/moving?agr=false").json()

    # Convert session data into DataFrames
    df = pd.DataFrame(response)

    # Find the last month in the DataFrame
    last_month = df["date"].max()

    # Filter the data for the last month
    df_last_month_imports = df[
        (df["date"] == last_month) & (df["moving_import_rank"] != 0)
    ]
    df_last_month_exports = df[
        (df["date"] == last_month) & (df["moving_export_rank"] != 0)
    ]

    # Sort the DataFrame by export and import rank, then select the top 5 items
    df_imports = df_last_month_imports.sort_values(by="moving_import_rank")
    df_exports = df_last_month_exports.sort_values(by="moving_export_rank")

    top5_imports = df_imports.head(5)
    top5_exports = df_exports.head(5)
    last5_imports = df_imports.tail(5)
    last5_exports = df_exports.tail(5)

    # Create histogram for top 5 export ranks
    fig_export_top = go.Figure()
    fig_export_top.add_trace(
        go.Bar(
            x=top5_exports["moving_price_exports"],
            y=top5_exports["hs4"],
            orientation="h",
            textposition="auto",
            name="Top Exports",
        )
    )

    fig_export_top.update_layout(
        title="Top 5 Items by Export Rank",
        xaxis_title="Export Price",
        yaxis_title="HTS Code",
        bargap=0.2,
    )

    # Create histogram for bottom 5 export ranks
    fig_export_bottom = go.Figure()
    fig_export_bottom.add_trace(
        go.Bar(
            x=last5_exports["moving_price_exports"],
            y=last5_exports["hs4"],
            orientation="h",
            textposition="auto",
            name="Bottom Exports",
        )
    )

    fig_export_bottom.update_layout(
        title="Bottom 5 Items by Export Rank",
        xaxis_title="Export Price",
        yaxis_title="HTS Code",
        bargap=0.2,
    )

    # Create histogram for top 5 import ranks
    fig_import_top = go.Figure()
    fig_import_top.add_trace(
        go.Bar(
            x=top5_imports["moving_price_imports"],
            y=top5_imports["hs4"],
            orientation="h",
            textposition="auto",
            name="Top Imports",
        )
    )
    fig_import_top.update_layout(
        title="Top 5 Items by Import Rank",
        xaxis_title="Import Price",
        yaxis_title="HTS Code",
        bargap=0.2,
    )

    # Create histogram for bottom 5 import ranks
    fig_import_bottom = go.Figure()
    fig_import_bottom.add_trace(
        go.Bar(
            x=last5_imports["moving_price_imports"],
            y=last5_imports["hs4"],
            orientation="h",
            textposition="auto",
            name="Bottom Imports",
        )
    )
    fig_import_bottom.update_layout(
        title="Bottom 5 Items by Import Rank",
        xaxis_title="Import Price",
        yaxis_title="HTS Code",
        bargap=0.2,
    )

    # Validate required columns
    return render(
        request,
        "productos_ranking.html",
        {
            "graph_export_top": fig_export_top.to_html(),
            "graph_export_bottom": fig_export_bottom.to_html(),
            "graph_import_top": fig_import_top.to_html(),
            "graph_import_bottom": fig_import_bottom.to_html(),
        },
    )

