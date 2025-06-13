import requests
from django.shortcuts import render
from env import get_db_credentials

creds = get_db_credentials()

API_URL = creds[6]


def web_app_awards(request):
    # URLs for each frequency

    # CATEGORY GRAPH
    if request.method == "POST":
        frequency = request.POST.get("frequency")
        category = request.POST.get("categories")
        second_dropdown = request.POST.get("second_dropdown")
        third_dropdown = request.POST.get("third_dropdown")

        if frequency is None and second_dropdown is None:
            frequency = "yearly"
            second_dropdown = 2013

        if category is None:
            category = 'awarding_agency_name'

        if frequency == 'yearly':
            year = second_dropdown
            period = 1
        else:
            year = third_dropdown
            period = second_dropdown
        
        category_graph, categories = requests.get(
            f"{API_URL}graph/awards/category/?dropdown={year}&second_dropdown={period}&third_dropdown={category}&time_frame={frequency}"
        ).json()
        
    else:
        category_graph, categories = requests.get(
            f"{API_URL}graph/awards/category/?dropdown=2013&second_dropdown=1&third_dropdown=awarding_agency_name&time_frame=yearly"
        ).json()

    # SECTER GRAPH
    if request.method == "POST":
        frequency_2 = request.POST.get("frequency_2")
        dropdown_2 = request.POST.get("agencies")

        if frequency_2 is None and dropdown_2 is None:
            frequency_2 = "yearly"
            dropdown_2 = 'department_of_defense'

        dropdown_2 = dropdown_2.lower().replace(" ", "_")

        secter_graph, agencies = requests.get(
            f"{API_URL}graph/awards/secter/?dropdown={dropdown_2}&time_frame={frequency_2}"
        ).json()
    else:
        secter_graph, agencies = requests.get(
            f"{API_URL}graph/awards/secter/?dropdown=department_of_defense&time_frame=yearly"
        ).json()


    # Validate required columns
    return render(request, "awards.html", {'sectergraph': secter_graph, 'categorygraph': category_graph, **agencies, **categories})

