from django.shortcuts import render
import requests
from env import get_db_credentials

creds = get_db_credentials()

api = creds[6]

def empleo_industria(request):
  if request.method == "POST":
    frequency = request.POST.get("frequency").lower()
    frequency_2 = request.POST.get("frequency_2").lower()
    frequency_3 = request.POST.get("frequency_3").lower()
    column = request.POST.get("columns")
    column_2 = request.POST.get("columns_2")
    column_3 = request.POST.get("columns_3")
    col = request.POST.get("type")
    col_2 = request.POST.get("type_2")
    col_3 = request.POST.get("type_3")
  else:
    frequency = "yearly"
    frequency_2 = "yearly"
    frequency_3 = "yearly"
    column = 'Accounting, Tax Preparation, Bookkeeping, and Payroll Services'
    column_2 = 'Accounting, Tax Preparation, Bookkeeping, and Payroll Services'
    column_3 = 'Accounting, Tax Preparation, Bookkeeping, and Payroll Services'
    col = 'taxable_wages'
    col_2 = 'taxable_wages'
    col_3 = 'taxable_wages'

  # Fetch graph from the API
  response = requests.get(f"{api}graph/nomina/?time_frame={frequency}&data_type=nivel&naics_desc={column}&column={col}").json()
  nomina_html, context = response

  response = requests.get(f"{api}graph/nomina/?time_frame={frequency_2}&data_type=cambio_porcentual&naics_desc={column_2}&column={col_2}").json()
  cambio_porcentual_html, context = response

  response = requests.get(f"{api}graph/nomina/?time_frame={frequency_3}&data_type=primera_diferencia&naics_desc={column_3}&column={col_3}").json()
  primera_diferencia_html, context = response

  return render(request, "empleo_industria.html", 
          {
              "nomina": nomina_html, 
              "api": api, 
              "cambio_porcentual": cambio_porcentual_html, 
              "primera_diferencia": primera_diferencia_html, 
              **context, 
              "selected_frequency": frequency, 
              "selected_frequency_2": frequency_2,
              "selected_frequency_3": frequency_3,
              "selected_column": column,
              "selected_column_2": column_2,
              "selected_column_3": column_3,
              "selected_col": col,
              "selected_col_2": col_2,
              "selected_col_3": col_3
          })