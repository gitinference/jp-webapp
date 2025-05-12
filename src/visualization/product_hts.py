import plotly.graph_objects as go
import pandas as pd
import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def fetch_trade_data(agg, hts_code):
    url = f"{API_URL}/data/trade/jp/?&time&types=hts&agr=false&group=false&data_filter={hts_code}&agg={agg}"
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        return pd.DataFrame()


def fetch_hts_codes():
    hts_codes_url = f"{API_URL}/data/trade/jp/hts_codes/"

    try:
        response = requests.get(hts_codes_url)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
    except ValueError as e:
        print(f"Error decoding JSON: {e}")
        return pd.DataFrame()


def sort_data(data, frequency, trade_type):
    data = data.sort_values(by=frequency, ascending=True)

    data["hts_code_first2"] = data["hts_code"].str[:2]
    data = data.sort_values(by=[frequency, "hts_code_first2"], ascending=[True, True])
    data = (
        data.groupby([frequency, "hts_code_first2"])
        .agg({trade_type: "sum"})
        .reset_index()
    )

    data = data[[frequency, "hts_code_first2", trade_type]]

    return data


def refactor_frequency(frequency):
    if frequency == "yearly":
        return "year"
    elif frequency == "monthly":
        return "month"
    elif frequency == "fiscal":
        return "fiscal_year"
    else:
        return frequency


def get_data_to_graph(frequency, hts_code, trade_type):
    data = fetch_trade_data(frequency, hts_code)
    print(data)
    new_frequency = refactor_frequency(frequency)
    data = sort_data(data, new_frequency, trade_type)

    x_axis = data[new_frequency]
    y_axis = data[trade_type]

    hts_list = fetch_hts_codes()

    context = {
        "hts_codes": hts_list["hts_code_first2"].tolist(),
    }

    return x_axis, y_axis, context


def products_hts(request):
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        hts_code = request.POST.get("hts_code")
        trade_type = request.POST.get("trade_type")
        print(
            f"Frequency: {frequency} | HTS Code: {hts_code} | Trade Type: {trade_type}"
        )

        x_axis, y_axis, context = get_data_to_graph(frequency, hts_code, trade_type)

    else:
        frequency = "yearly"
        hts_code = "01"
        trade_type = "imports"
        print(
            f"Frequency: {frequency} | HTS Code: {hts_code} | Trade Type: {trade_type}"
        )

        x_axis, y_axis, context = get_data_to_graph(frequency, hts_code, trade_type)

    frequency = frequency.capitalize()
    trade_type = trade_type.capitalize()
    title = f"Frequency: {frequency} | HTS Code: {hts_code} | Trade Type: {trade_type}"

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_axis, y=y_axis, mode="lines+markers"))

    fig.update_layout(title=title)

    return render(request, "product_hts.html", {"graph": fig.to_html(), **context})

