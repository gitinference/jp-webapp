import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def web_app_awards(request):
    # URLs for each frequency

    # CATEGORY GRAPH
    if request.method == "POST":
        frequency = request.POST.get("frequency").lower()
        category = request.POST.get("categories")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")

        if frequency is None and second_dropdown is None:
            frequency = "yearly"
            second_dropdown = 2009

        if category is None:
            category = 'awarding_agency_name'

        if frequency == 'yearly' or frequency == 'fiscal':
            year = second_dropdown
            period = 1
        else:
            year = third_dropdown
            period = second_dropdown
        
        category_graph, categories = requests.get(
            f"{API_URL}graph/awards/category/?dropdown={year}&second_dropdown={period}&third_dropdown={category}&time_frame={frequency}"
        ).json()
        
    else:
        frequency = "yearly"
        second_dropdown = 2009
        third_dropdown = 1
        category = 'awarding_agency_name'
        category_graph, categories = requests.get(
            f"{API_URL}graph/awards/category/?dropdown={second_dropdown}&second_dropdown={third_dropdown}&third_dropdown={category}&time_frame={frequency}"
        ).json()

    # SECTER GRAPH
    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2").lower()
        dropdown_2 = request.POST.get("agencies")

        if frequency_2 is None and dropdown_2 is None:
            frequency_2 = "yearly"
            dropdown_2 = 'total'

        temp_dropdown_2 = dropdown_2.lower().replace(" ", "_")

        secter_graph, agencies = requests.get(
            f"{API_URL}graph/awards/secter/?dropdown={temp_dropdown_2}&time_frame={frequency_2}"
        ).json()
    else:
        frequency_2 = "yearly"
        dropdown_2 = 'total'
        secter_graph, agencies = requests.get(
            f"{API_URL}graph/awards/secter/?dropdown={dropdown_2}&time_frame={frequency_2}"
        ).json()

    secter_graph = f"<div style='overflow-x: auto; white-space: nowrap; width: 100%; padding-bottom: 20px;'>{secter_graph}</div>"

    # Validate required columns
    return render(request, "awards.html", 
                    {
                      'sectergraph': secter_graph, 
                      'categorygraph': category_graph, 
                      **agencies, 
                      **categories, 
                      "api":API_URL,
                      'selected_frequency': frequency,
                      'selected_second_dropdown': second_dropdown,
                      'selected_third_dropdown': third_dropdown,
                      'selected_category': category,
                      'selected_frequency_2': frequency_2,
                      'selected_dropdown_2': dropdown_2
                    })

