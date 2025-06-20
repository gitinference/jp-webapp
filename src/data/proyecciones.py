from django.shortcuts import render
import plotly.graph_objects as go
import pandas as pd

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
        title="Gráfica Anual",
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
        title="Gráfica Mensual",
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
        title="Gráfica Año Fiscal",
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
        title="Gráfica Trimestral",
        xaxis_title=" ",
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

def proyecciones_poblacionales(request):

    d_table = demographic_table(request)
    annual_graph = projection_annual_graph()
    monthly_graph = projection_monthly_graph()
    fiscal_graph = projection_fiscal_graph()
    quarter_graph = projection_quarter_graph()

    context = {
        "d_table": d_table,
        "annual_graph": annual_graph,
        "monthly_graph": monthly_graph,
        "fiscal_graph": fiscal_graph,
        "quarter_graph": quarter_graph
        }
    
    return render(request, "proyecciones.html", context)

def demographic_table(request):
    df = pd.read_parquet("data/processed/fiscal_year_idb.parquet")
    demographic_table = df.to_html(index=False, classes='table table-striped')
    return demographic_table