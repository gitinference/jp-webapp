from django.shortcuts import render
from src.dao.data_db_dao import DAO
import csv
import os


def IP_220(request):
    if request.method == "POST":
        # Retrieve form data
        company_name = request.POST.get("company_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        liaison_officer = request.POST.get("liaison_officer")
        ssn = request.POST.get("ssn")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        legal_form = request.POST.get("legal_form")
        cfc = request.POST.get("cfc")
        business_type = request.POST.get("business_type")
        business_function = request.POST.get("business_function")
        branches = request.POST.get("branches")
        branches_yes = request.POST.get("branches_yes")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")
        services_revenues_12 = request.POST.get("services_revenues_12")
        services_revenues_13 = request.POST.get("services_revenues_13")
        residential_consumers_12 = request.POST.get("residential_consumers_12")
        residential_consumers_13 = request.POST.get("residential_consumers_13")
        other_consumers_12 = request.POST.get("other_consumers_12")
        other_consumers_13 = request.POST.get("other_consumers_13")
        incomes_rents_12 = request.POST.get("incomes_rents_12")
        incomes_rents_13 = request.POST.get("incomes_rents_13")
        incomes_interests_12 = request.POST.get("incomes_interests_12")
        incomes_interests_13 = request.POST.get("incomes_interests_13")
        dividends_12 = request.POST.get("dividends_12")
        dividends_13 = request.POST.get("dividends_13")
        others_incomes_12 = request.POST.get("others_incomes_12")
        others_incomes_13 = request.POST.get("others_incomes_13")
        total_income_12 = request.POST.get("total_income_12")
        total_income_13 = request.POST.get("total_income_13")
        salaries_2012 = request.POST.get("salaries_2012")
        salaries_2013 = request.POST.get("salaries_2013")
        expenses_interests_12 = request.POST.get("expenses_interests_12")
        expenses_interests_13 = request.POST.get("expenses_interests_13")
        expenses_rents_12 = request.POST.get("expenses_rents_12")
        expenses_rents_13 = request.POST.get("expenses_rents_13")
        depreciation_12 = request.POST.get("depreciation_12")
        depreciation_13 = request.POST.get("depreciation_13")
        bad_debts_12 = request.POST.get("bad_debts_12")
        bad_debts_13 = request.POST.get("bad_debts_13")
        donations_12 = request.POST.get("donations_12")
        donations_13 = request.POST.get("donations_13")
        sales_tax_12 = request.POST.get("sales_tax_12")
        sales_tax_13 = request.POST.get("sales_tax_13")
        machinery_12 = request.POST.get("machinery_12")
        machinery_13 = request.POST.get("machinery_13")
        other_purchases_12 = request.POST.get("other_purchases_12")
        other_purchases_13 = request.POST.get("other_purchases_13")
        licenses_12 = request.POST.get("licenses_12")
        licenses_13 = request.POST.get("licenses_13")
        other_expenses_12 = request.POST.get("other_expenses_12")
        other_expenses_13 = request.POST.get("other_expenses_13")
        total_expenses_12 = request.POST.get("total_expenses_12")
        total_expenses_13 = request.POST.get("total_expenses_13")
        net_profit_12 = request.POST.get("net_profit_12")
        net_profit_13 = request.POST.get("net_profit_13")
        income_tax_12 = request.POST.get("income_tax_12")
        income_tax_13 = request.POST.get("income_tax_13")
        profit_after_tax_12 = request.POST.get("profit_after_tax_12")
        profit_after_tax_13 = request.POST.get("profit_after_tax_13")
        withheld_tax_12 = request.POST.get("withheld_tax_12")
        withheld_tax_13 = request.POST.get("withheld_tax_13")
        signature = request.POST.get("signature")
        rank = request.POST.get("rank")

        csv_file_path = "data/cuestionarios/ingreso_neto/IP-220.csv"
        file_exists = (
            os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0
        )

        with open(csv_file_path, mode="a", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(
                    [
                        "company_name",
                        "address",
                        "email",
                        "liaison_officer",
                        "ssn",
                        "tel",
                        "fax",
                        "legal_form",
                        "cfc",
                        "business_type",
                        "business_function",
                        "branches",
                        "branches_yes",
                        "closing_date",
                        "start_year",
                        "end_year",
                        "services_revenues_12",
                        "services_revenues_13",
                        "residential_consumers_12",
                        "residential_consumers_13",
                        "other_consumers_12",
                        "other_consumers_13",
                        "incomes_rents_12",
                        "incomes_rents_13",
                        "incomes_interests_12",
                        "incomes_interests_13",
                        "dividends_12",
                        "dividends_13",
                        "others_incomes_12",
                        "others_incomes_13",
                        "total_income_12",
                        "total_income_13",
                        "salaries_2012",
                        "salaries_2013",
                        "expenses_interests_12",
                        "expenses_interests_13",
                        "expenses_rents_12",
                        "expenses_rents_13",
                        "depreciation_12",
                        "depreciation_13",
                        "bad_debts_12",
                        "bad_debts_13",
                        "donations_12",
                        "donations_13",
                        "sales_tax_12",
                        "sales_tax_13",
                        "machinery_12",
                        "machinery_13",
                        "other_purchases_12",
                        "other_purchases_13",
                        "licenses_12",
                        "licenses_13",
                        "other_expenses_12",
                        "other_expenses_13",
                        "total_expenses_12",
                        "total_expenses_13",
                        "net_profit_12",
                        "net_profit_13",
                        "income_tax_12",
                        "income_tax_13",
                        "profit_after_tax_12",
                        "profit_after_tax_13",
                        "withheld_tax_12",
                        "withheld_tax_13",
                        "signature",
                        "rank",
                    ]
                )

            writer.writerow(
                [
                    company_name,
                    address,
                    email,
                    liaison_officer,
                    ssn,
                    tel,
                    fax,
                    legal_form,
                    cfc,
                    business_type,
                    business_function,
                    branches,
                    branches_yes,
                    closing_date,
                    start_year,
                    end_year,
                    services_revenues_12,
                    services_revenues_13,
                    residential_consumers_12,
                    residential_consumers_13,
                    other_consumers_12,
                    other_consumers_13,
                    incomes_rents_12,
                    incomes_rents_13,
                    incomes_interests_12,
                    incomes_interests_13,
                    dividends_12,
                    dividends_13,
                    others_incomes_12,
                    others_incomes_13,
                    total_income_12,
                    total_income_13,
                    salaries_2012,
                    salaries_2013,
                    expenses_interests_12,
                    expenses_interests_13,
                    expenses_rents_12,
                    expenses_rents_13,
                    depreciation_12,
                    depreciation_13,
                    bad_debts_12,
                    bad_debts_13,
                    donations_12,
                    donations_13,
                    sales_tax_12,
                    sales_tax_13,
                    machinery_12,
                    machinery_13,
                    other_purchases_12,
                    other_purchases_13,
                    licenses_12,
                    licenses_13,
                    other_expenses_12,
                    other_expenses_13,
                    total_expenses_12,
                    total_expenses_13,
                    net_profit_12,
                    net_profit_13,
                    income_tax_12,
                    income_tax_13,
                    profit_after_tax_12,
                    profit_after_tax_13,
                    withheld_tax_12,
                    withheld_tax_13,
                    signature,
                    rank,
                ]
            )

        DAO().insert_forms(
            data_path="data/cuestionarios/ingreso_neto/IP-220.csv",
            dtypes={
                "company_name": str,
                "address": str,
                "email": str,
                "liaison_officer": str,
                "ssn": str,
                "tel": str,
                "fax": str,
                "legal_form": str,
                "cfc": str,
                "business_type": str,
                "business_function": str,
                "branches": str,
                "branches_yes": str,
                "closing_date": str,
                "start_year": int,
                "end_year": int,
                "services_revenues_12": float,
                "services_revenues_13": float,
                "residential_consumers_12": float,
                "residential_consumers_13": float,
                "other_consumers_12": float,
                "other_consumers_13": float,
                "incomes_rents_12": float,
                "incomes_rents_13": float,
                "incomes_interests_12": float,
                "incomes_interests_13": float,
                "dividends_12": float,
                "dividends_13": float,
                "others_incomes_12": float,
                "others_incomes_13": float,
                "total_income_12": float,
                "total_income_13": float,
                "salaries_2012": float,
                "salaries_2013": float,
                "expenses_interests_12": float,
                "expenses_interests_13": float,
                "expenses_rents_12": float,
                "expenses_rents_13": float,
                "depreciation_12": float,
                "depreciation_13": float,
                "bad_debts_12": float,
                "bad_debts_13": float,
                "donations_12": float,
                "donations_13": float,
                "sales_tax_12": float,
                "sales_tax_13": float,
                "machinery_12": float,
                "machinery_13": float,
                "other_purchases_12": float,
                "other_purchases_13": float,
                "licenses_12": float,
                "licenses_13": float,
                "other_expenses_12": float,
                "other_expenses_13": float,
                "total_expenses_12": float,
                "total_expenses_13": float,
                "net_profit_12": float,
                "net_profit_13": float,
                "income_tax_12": float,
                "income_tax_13": float,
                "profit_after_tax_12": float,
                "profit_after_tax_13": float,
                "withheld_tax_12": float,
                "withheld_tax_13": float,
                "signature": str,
                "rank": str,
            },
            table_name="IP_220",
            table_id="17",
            debug=False,
        )

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-220.html")
