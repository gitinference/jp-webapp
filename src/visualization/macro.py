import pandas as pd
from django.http import HttpResponse, FileResponse
from django.shortcuts import render

import plotly.graph_objects as go
import plotly.express as px
import os

def web_app_macro(request):
  
    # FIRST GRAPH DATA 
    df1 = pd.read_parquet("data/processed/series-historicas-2001-2023_processed.parquet").sort_values(by="PERIODO = AÑO FISCAL").reset_index()
    for i in df1.columns:
        df1[i] = df1[i].astype(float)
        
    y_axis_options_1 = sorted(df1.columns[2:], reverse=True)
    x_axis_1 = df1["PERIODO = AÑO FISCAL"]
    y_axis_1 = df1[y_axis_options_1[0]]

    # FIRST GRAPH SETTINGS
    fig1 = px.scatter(x=x_axis_1, y=y_axis_1)
    fig1.add_trace(go.Scatter(
        x=x_axis_1,
        y=y_axis_1,
        mode='lines+markers',
        line=dict(color='#FF2525', width=3),
        marker=dict(size=4, color='#00cdf1'),
        hoverinfo='text',
    ))

    fig1.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='#F7F7F7',
        hovermode='x',
        showlegend=False,
        xaxis=dict(
            title="",
            color='black',
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        yaxis=dict(
            title="",
            color='black',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        width=1380,
    )

    fig1.update_layout(
        annotations=[
            dict(
                x=0.01,
                y=1.11,
                xref='paper',
                yref='paper',
                text='Y:',
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            )
        ],
        updatemenus=[
            dict(
                buttons=[
                    dict(
                        args=[{"y": [df1[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_options_1
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.07,
                xanchor="left",
                y=1.15,
                yanchor="top"
            )
        ]
    )
    # --------------------------------------------------------------------------------------------------------------------------------
    
    # SECOND GRAPH DATA
    df2 = pd.read_parquet("data/processed/series-historicas-1950-2011_processed.parquet").sort_values(by="PERIODO = AÑO FISCAL").reset_index()
    for i in df2.columns:
        df2[i] = df2[i].astype(float)
        
    y_axis_options_2 = sorted(df2.columns[2:], reverse=True)
    x_axis_2 = df2["PERIODO = AÑO FISCAL"]
    y_axis_2 = df2[y_axis_options_2[0]]
    
    #  SECOND GRAPH SETTINGS
    fig2 = px.scatter(x=x_axis_2, y=y_axis_2)
    fig2.add_trace(go.Scatter(
        x=x_axis_2,
        y=y_axis_2,
        mode='lines+markers',
        line=dict(color='#FF2525', width=3),
        marker=dict(size=4, color='#00cdf1'),
        hoverinfo='text',
    ))

    fig2.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        plot_bgcolor='#F7F7F7',
        hovermode='x',
        showlegend=False,
        xaxis=dict(
            title="",
            color='black',
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        yaxis=dict(
            title="",
            color='black',
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='black',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
        ),
        width=1370
    )

    fig2.update_layout(
        annotations=[
            dict(
                x=0.01,
                y=1.11,
                xref='paper',
                yref='paper',
                text='Y:',
                showarrow=False,
                font=dict(
                    family='Arial',
                    size=18,
                    color='black'
                ),
                xanchor='left',
                yanchor='top'
            )
        ],
        updatemenus=[
            dict(
                buttons=[
                    dict(
                        args=[{"y": [df2[col]]}],
                        label=col,
                        method="update"
                    ) for col in y_axis_options_2
                ],
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.07,
                xanchor="left",
                y=1.15,
                yanchor="top"
            )
        ]
    )

    macro_html_1 = fig1.to_html()
    macro_html_2 = fig2.to_html()
    
    if request.method == "POST":
        historicas = request.POST.get("historicas")
        if(historicas == "2011"):
            file_path = "data/processed/series-historicas-1950-2011_processed.parquet"
        elif(historicas == "2023"):
            file_path = "data/processed/series-historicas-2001-2023_processed.parquet"
        else:
            file_path = None
        
        csv_path = os.path.splitext(file_path)[0] + ".csv"
        if not os.path.exists(csv_path):
            df = pd.read_parquet(file_path)
            df.to_csv(csv_path, index=False)
        return FileResponse(open(csv_path, 'rb'), as_attachment=True, filename=os.path.basename(csv_path))

    context = {
        "macro1": macro_html_1,
        "macro2": macro_html_2,
    }
    return render(request, "macro.html", context)
