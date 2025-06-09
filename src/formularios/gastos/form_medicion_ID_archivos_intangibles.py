from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os

def Medicion_ID_archivos_intangibles(request): # Cambia
    # if request.method == "POST":
    #     # Retrieve form data
    #     # income_expenses_year_1 = request.POST["income_expenses_year_1"]

    #     csv_file_path = "data/cuestionarios/balanza_de_pagos/JP_362_qtr.csv" # Cambia
    #     file_exists = (
    #         os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
    #     )

    #     with open(csv_file_path, mode="a", newline="") as file:
    #         writer = csv.writer(file)

    #         if not file_exists:
    #             writer.writerow(
    #                 [
    #                     "income_expenses_year_1", # Cambia
            
    #                 ]
    #             )

    #         writer.writerow(
    #             [
    #                 # income_expenses_year_1,
                   
    #             ]
    #         )

    #     DAO().insert_forms(
    #         data_path="data/cuestionarios/balanza_de_pagos/JP_361_qrt.csv", # Cambia
    #         dtypes={
    #                 # income_expenses_year_1: int,
                
                    
    #         },
    #         table_name="JP_362_qtr", # Cambia
    #         table_id="60", # Cambia
    #         debug=False,
    #     )

    #     return render(request, "forms/succesfull.html")
    return render(request, "forms/gastos/Medicion_ID_archivos_intangibles.html") # Cambia
