import plotly.graph_objects as go
import pandas as pd

def demographic_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/Anual_Historico.csv")
    
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
        xaxis_title="Demográfico",
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
        for i, y_column in enumerate(y_columns)
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
    demographic_graph_html = fig.to_html(full_html=False)
    
    return demographic_graph_html

def trimestral_demographic_graph(selected_graph=1):
    # Read the new CSV file
    df = pd.read_csv("data/external/Trimestral_Historico.csv")

    # Extract column names
    columns = df.columns
    
    # Ensure the year and quarter columns are of correct type
    year= df[columns[0]].astype(str)
    qrt = df[columns[1]].astype(str)

    # Create a new column for the formatted x-axis
    df['YearQuarter'] = year + "Q" + qrt
    
    # The new column is the x-axis
    x_column = 'YearQuarter'
    
    # The rest of the columns are y-axes
    y_columns = columns[2:]

    # Create figure
    fig = go.Figure()

    # Add traces for each y-axis column
    for i, y_column in enumerate(y_columns):
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))

    # Create dropdown menu options to toggle traces on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]

    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )

    # Update layout with the updatemenus dropdown and range slider
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ],
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"  # Use "category" type for year-quarter format
        ),
        title="Gráfica Trimestral",
        xaxis_title="Trimestre",
        yaxis_title=" ",
        width=1500,
        height=750
    )

    # Convert the figure to HTML
    trimestral_demographic_graph_html = fig.to_html(full_html=False)
    return trimestral_demographic_graph_html

def monthly_demographic_graph():
    # Read the new CSV file
    df = pd.read_csv("data/external/Mensual_Historico.csv")

    # Extract column names
    columns = df.columns
    
    # Ensure the year and quarter columns are of correct type
    year= df[columns[0]].astype(str)
    month = df[columns[1]].astype(str)

    # Create a new column for the formatted x-axis
    df['Year/Month'] = year + "M" + month
    
    # The new column is the x-axis
    x_column = 'Year/Month'
    
    # The rest of the columns are y-axes
    y_columns = columns[2:]

    # Create figure
    fig = go.Figure()

    # Add traces for each y-axis column
    for i, y_column in enumerate(y_columns):
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=y_column))

    # Create dropdown menu options to toggle traces on or off
    update_menu = [
        dict(label=f"Show {y_column}",
             method="update",
             args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Showing {y_column}"}])
        for i, y_column in enumerate(y_columns)
    ]

    # Add a "Show All" button to display all traces
    update_menu.append(
        dict(label="Show All",
             method="update",
             args=[{"visible": [True] * len(y_columns)},  # Show all traces
                   {"title": "All Y-Axis Columns"}])
    )

    # Update layout with the updatemenus dropdown and range slider
    fig.update_layout(
        updatemenus=[
            dict(
                buttons=update_menu,
                direction="down",
                showactive=True
            )
        ],
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="category"  # Use "category" type for year-quarter format
        ),
        title="Gráfica Mensual",
        xaxis_title="Mensual",
        yaxis_title=" ",
        width=1500,
        height=750
    )
    
    # Convert the figure to HTML
    monthly_demographic_graph_html = fig.to_html(full_html=False)
    return monthly_demographic_graph_html

def fiscal_demographic_graph():
    # Read the CSV file
    df = pd.read_csv("data/external/Fiscal_Historico.csv")
    
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
        for i, y_column in enumerate(y_columns)
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
    fiscal_demographic_graph_html = fig.to_html(full_html=False)
    
    return fiscal_demographic_graph_html