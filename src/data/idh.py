import plotly.graph_objects as go
import pandas as pd


def normal_indexes_graph():
    # Read your CSV file
    df = pd.read_csv("data/processed/idh_index.csv")

    # Extract column names
    columns = df.columns
    
    # Ensure the 'Year' column is of the correct type for the x-axis
    df['Year'] = df['Year'].astype(str)

    # The 'Year' column will be the x-axis
    x_column = 'Year'
    
    # The remaining columns represent y-axes (all the index columns)
    
    y_columns = columns[1::2]  # Starts from the second column and selects every second column
    
    index_names = {
        'health_index': 'Índice de Salud',
        'income_index': 'Índice de Ingresos',
        'edu_index': 'Índice de Educación',
        'index': 'Índice de Desarrollo',
        'growth_rate': 'Tasa de Crecimiento'
    }

    # Create a figure
    fig = go.Figure()
    
    # Create dropdown menu options to toggle traces on or off
    update_menu = [
        dict(label=f"Mostrar {index_names.get(y_column, y_column)}",
             method="update",
             args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Mostrando {index_names.get(y_column, y_column)}"}])
        for i, y_column in enumerate(y_columns)
    ]

    # # Add a "Show All" button to display all traces
    # update_menu.append(
    #     dict(label="Mostrar todo",
    #          method="update",
    #          args=[{"visible": [True] * len(y_columns)},  # Show all traces
    #                {"title": "Todas las Columnas"}])
    # )

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
        title="",
        xaxis_title="",
        yaxis_title=" ",
        width=1500,
        height=750
    )

   # Add traces for each y-axis column
    for i, y_column in enumerate(y_columns):
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=index_names.get(y_column, y_column)))
        
    # Update the layout to remove explicit width settings
    fig.update_layout(
        autosize=True,        # Automatically adjust the size
        width=None,           # Do not set a fixed width
        height=None,          # Ensure it adapts to container height
        margin=dict(l=20, r=20, t=30, b=30)  # Adjust margins if needed
    )

    # Convert the figure to HTML
    html_normal_indexes = fig.to_html(full_html=False)
    return html_normal_indexes

def adjusted_indexes_graph():
    # Read your CSV file
    df = pd.read_csv("data/processed/idh_index.csv")

    # Extract column names
    columns = df.columns
    
    # Ensure the 'Year' column is of the correct type for the x-axis
    df['Year'] = df['Year'].astype(str)

    # The 'Year' column will be the x-axis
    x_column = 'Year'
    
    # The remaining columns represent y-axes (all the index columns)
    y_columns = columns[2::2]  # Starts from the second column and selects every second column
    
    adjusted_index_names = {
        'health_index_adjusted': 'Índice de Salud Ajustado',
        'income_index_ajusted': 'Índice de Ingresos Ajustado',
        'edu_index_ajusted': 'Índice de Educación Ajustado',
        'index_ajusted': 'Índice de Desarrollo Ajustado',  
        'growth_rate_ajusted': 'Tasa de Crecimiento Ajustada'    
    }

    # Create a figure
    fig = go.Figure()
    
     # Create dropdown menu options to toggle traces on or off
    update_menu = [
        dict(label=f"Mostrar {adjusted_index_names.get(y_column, y_column)}",
             method="update",
             args=[{"visible": [i == idx or False for idx in range(len(y_columns))]},  # Make the selected trace visible
                   {"title": f"Mostrando {adjusted_index_names.get(y_column, y_column)}"}])
        for i, y_column in enumerate(y_columns)
    ]

    # # Add a "Show All" button to display all traces
    # update_menu.append(
    #     dict(label="Mostrar todo",
    #          method="update",
    #          args=[{"visible": [True] * len(y_columns)},  # Show all traces
    #                {"title": "Todas las Columnas"}])
    # )

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
        title="",
        xaxis_title="",
        yaxis_title=" ",
        width=1500,
        height=750
    )

   # Add traces for each y-axis column
    for i, y_column in enumerate(y_columns):
        fig.add_trace(go.Scatter(x=df[x_column], y=df[y_column], name=adjusted_index_names.get(y_column, y_column)))
        
            # Update the layout to remove explicit width settings
    fig.update_layout(
        autosize=True,        # Automatically adjust the size
        width=None,           # Do not set a fixed width
        height=None,          # Ensure it adapts to container height
        margin=dict(l=20, r=20, t=30, b=30)  # Adjust margins if needed
    )

    # Convert the figure to HTML
    html_normal_indexes = fig.to_html(full_html=False)
    return html_normal_indexes
