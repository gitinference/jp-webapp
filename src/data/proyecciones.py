from django.shortcuts import render
from django.http import HttpResponse, FileResponse

import plotly.graph_objects as go
import pandas as pd
import os

def projection_annual_graph():
    # Read the CSV file
    df = pd.read_parquet("data/external/yearly_idb.parquet")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date"
        ),
        # title="Gráfica Anual",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(sorted(y_columns))
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_annual_html = fig.to_html(full_html=False)
    
    return projection_annual_html

def projection_monthly_graph():
    # Read the CSV file
    df = pd.read_parquet("data/external/monthly_idb.parquet")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    df[x_column] = df[x_column].astype(str)

    # The rest of the columns are y-axes
    y_columns = columns[1:]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        # title="Gráfica Mensual",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(sorted(y_columns))
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_monthly_html = fig.to_html(full_html=False)
    return projection_monthly_html

def projection_fiscal_graph():
    # Read the CSV file
    df = pd.read_parquet("data/external/fiscal_year_idb.parquet")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]
    
    # The rest of the columns are y-axes
    y_columns = columns[1:5]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        # title="Gráfica Año Fiscal",
        xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    annotations = [
        dict(x="2022-01-01", y=100, xref="x", yref="y",
             text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(sorted(y_columns))
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_fiscal_html = fig.to_html(full_html=False)
    
    return projection_fiscal_html

def projection_quarter_graph():
    # Read the CSV file
    df = pd.read_parquet("data/external/quarterly_idb.parquet")
    
    # Extract column names
    columns = df.columns
    
    # The new column is the x-axis
    x_column = columns[0]

    df[x_column] = df[x_column].astype(str)
    
    # The rest of the columns are y-axes
    y_columns = columns[1:]
    
    # Create the graph
    fig = go.Figure()
    
    for y_column in y_columns:
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))
    
    # Update layout with range slider and selectors
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"
        ),
        # title="Gráfica Trimestral",
        # xaxis_title=" ",
        yaxis_title=" ",
        width=1400,
        height=750
    )
    
    # Add Annotations (if needed, for now static)
    # annotations = [
    #     dict(x="2022-01-01", y=100, xref="x", yref="y",
    #          text="Annotation Text", showarrow=True, arrowhead=1, ax=0, ay=-40)
    # ]
    
    # Create the button options to toggle y-columns on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or vis for idx, vis in enumerate([False] * len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(sorted(y_columns))
    ]
    
    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )
    
    # Update layout with the updatemenus dropdown
    fig.update_layout(
        updatemenus=[
            dict(
                active=0,
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ]
    )
    
    # Convert the figure to HTML
    projection_quarter_html = fig.to_html(full_html=True)
    
    return projection_quarter_html

def proyecciones_poblacionales(valor):
    grafica_html = ""
    if valor == "anual":
        grafica_html = projection_annual_graph()
    elif valor == "semestral":
        grafica_html = projection_quarter_graph()
    elif valor == "mensual":
        grafica_html = projection_monthly_graph()
    elif valor == "fiscal":
        grafica_html = projection_fiscal_graph()
   
    return grafica_html

def demographic_table(request):
    df = pd.read_parquet("data/processed/fiscal_year_idb.parquet")
    demographic_table = df.to_html(index=False, classes='table table-striped')
    return demographic_table

def proyecciones_accion(request):
    grafica_html = proyecciones_poblacionales('anual')
    selected = "anual"  # Default value for the period type
    valor ="anual"

    if request.method == "POST":
        valor = request.POST.get("tipo_periodo")
        accion = request.POST.get("accion")

        # Selección de archivo Parquet según el valor
        if valor == "anual":
            file_path = "data/processed/yearly_idb.parquet"
        elif valor == "semestral":
            file_path = "data/processed/quarterly_idb.parquet"
        elif valor == "mensual":
            file_path = "data/processed/monthly_idb.parquet"
        elif valor == "fiscal":
            file_path = "data/processed/fiscal_year_idb.parquet"
        else:
            file_path = None

        if not file_path or not os.path.exists(file_path):
            return HttpResponse("Seleccione un periodo válido o el archivo no existe", status=400)
        
        if accion == "grafica":
            grafica_html = proyecciones_poblacionales(valor)
            selected = valor 
        elif accion == "csv":
            csv_path = os.path.splitext(file_path)[0] + ".csv"
            if not os.path.exists(csv_path):
                df = pd.read_parquet(file_path)
                df.to_csv(csv_path, index=False)
            return FileResponse(open(csv_path, 'rb'), as_attachment=True, filename=os.path.basename(csv_path))  
    
    return render(request, "proyecciones.html", {"grafica_html": grafica_html, "selected": selected, "valor":valor})