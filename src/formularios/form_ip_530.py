from django.shortcuts import render
from src.dao.data_db_dao import DAO
import polars as pl

def IP_530(request):
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
        other_business_type = request.POST.get("other_business_type")
        closing_date = request.POST.get("closing_date")
        start_year = request.POST.get("start_year")
        end_year = request.POST.get("end_year")

        incomes_from_persons_1 = request.POST.get("incomes_from_persons_1")
        incomes_from_persons_2 = request.POST.get("incomes_from_persons_2")
        incomes_industries_businesses_1 = request.POST.get(
            "incomes_industries_businesses_1"
        )
        incomes_industries_businesses_2 = request.POST.get(
            "incomes_industries_businesses_2"
        )
        incomes_rent_1 = request.POST.get("incomes_rent_1")
        incomes_rent_2 = request.POST.get("incomes_rent_2")
        incomes_interests_1 = request.POST.get("incomes_interests_1")
        incomes_interests_2 = request.POST.get("incomes_interests_2")
        incomes_comissions_1 = request.POST.get("incomes_comissions_1")
        incomes_comissions_2 = request.POST.get("incomes_comissions_2")
        incomes_gain_loss_1 = request.POST.get("incomes_gain_loss_1")
        incomes_gain_loss_2 = request.POST.get("incomes_gain_loss_2")
        incomes_operating_1 = request.POST.get("incomes_operating_1")
        incomes_operating_2 = request.POST.get("incomes_operating_2")
        expenses_salaries_wages_bonus_1 = request.POST.get(
            "expenses_salaries_wages_bonus_1"
        )
        expenses_salaries_wages_bonus_2 = request.POST.get(
            "expenses_salaries_wages_bonus_2"
        )
        expenses_interests_1 = request.POST.get("expenses_interests_1")
        expenses_interests_2 = request.POST.get("expenses_interests_2")
        expenses_rent_1 = request.POST.get("expenses_rent_1")
        expenses_rent_2 = request.POST.get("expenses_rent_2")
        expenses_depreciation_1 = request.POST.get("expenses_depreciation_1")
        expenses_depreciation_2 = request.POST.get("expenses_depreciation_2")
        expenses_donations_1 = request.POST.get("expenses_donations_1")
        expenses_donations_2 = request.POST.get("expenses_donations_2")
        expenses_sales_tax_1 = request.POST.get("expenses_sales_tax_1")
        expenses_sales_tax_2 = request.POST.get("expenses_sales_tax_2")
        expenses_machinary_equipment_1 = request.POST.get(
            "expenses_machinary_equipment_1"
        )
        expenses_machinary_equipment_2 = request.POST.get(
            "expenses_machinary_equipment_2"
        )
        expenses_other_purchases_1 = request.POST.get("expenses_other_purchases_1")
        expenses_other_purchases_2 = request.POST.get("expenses_other_purchases_2")
        expenses_licenses_1 = request.POST.get("expenses_licenses_1")
        expenses_licenses_2 = request.POST.get("expenses_licenses_2")
        expenses_other_operations_1 = request.POST.get("expenses_other_operations_1")
        expenses_other_operations_2 = request.POST.get("expenses_other_operations_2")
        expenses_total_1 = request.POST.get("expenses_total_1")
        expenses_total_2 = request.POST.get("expenses_total_2")
        gross_profit_1 = request.POST.get("gross_profit_1")
        gross_profit_2 = request.POST.get("gross_profit_2")
        profit_income_tax_1 = request.POST.get("profit_income_tax_1")
        profit_income_tax_2 = request.POST.get("profit_income_tax_2")
        profit_after_income_tax_1 = request.POST.get("profit_after_income_tax_1")
        profit_after_income_tax_2 = request.POST.get("profit_after_income_tax_2")
        sales_tax_withheld_1 = request.POST.get("sales_tax_withheld_1")
        sales_tax_withheld_2 = request.POST.get("sales_tax_withheld_2")

        name = request.POST.get("name")
        rank = request.POST.get("rank")

        data = [
            pl.Series("company_name", [company_name], dtype=pl.String),
            pl.Series("address", [address], dtype=pl.String),
            pl.Series("email", [email], dtype=pl.String),
            pl.Series("liaison_officer", [liaison_officer], dtype=pl.String),
            pl.Series("ssn", [ssn], dtype=pl.String),
            pl.Series("tel", [tel], dtype=pl.String),
            pl.Series("fax", [fax], dtype=pl.String),
            pl.Series("legal_form", [legal_form], dtype=pl.String),
            pl.Series("cfc", [cfc], dtype=pl.String),
            pl.Series("business_type", [business_type], dtype=pl.String),
            pl.Series("other_business_type", [other_business_type], dtype=pl.String),
            pl.Series("closing_date", [closing_date], dtype=pl.String),
            pl.Series("start_year", [start_year], dtype=pl.String),
            pl.Series("end_year", [end_year], dtype=pl.String),
            pl.Series("incomes_from_persons_1", [float(incomes_from_persons_1)], dtype=pl.Float64),
            pl.Series("incomes_from_persons_2", [float(incomes_from_persons_2)], dtype=pl.Float64),
            pl.Series("incomes_industries_businesses_1", [float(incomes_industries_businesses_1)], dtype=pl.Float64),
            pl.Series("incomes_industries_businesses_2", [float(incomes_industries_businesses_2)], dtype=pl.Float64),
            pl.Series("incomes_rent_1", [float(incomes_rent_1)], dtype=pl.Float64),
            pl.Series("incomes_rent_2", [float(incomes_rent_2)], dtype=pl.Float64),
            pl.Series("incomes_interests_1", [float(incomes_interests_1)], dtype=pl.Float64),
            pl.Series("incomes_interests_2", [float(incomes_interests_2)], dtype=pl.Float64),
            pl.Series("incomes_comissions_1", [float(incomes_comissions_1)], dtype=pl.Float64),
            pl.Series("incomes_comissions_2", [float(incomes_comissions_2)], dtype=pl.Float64),
            pl.Series("incomes_gain_loss_1", [float(incomes_gain_loss_1)], dtype=pl.Float64),
            pl.Series("incomes_gain_loss_2", [float(incomes_gain_loss_2)], dtype=pl.Float64),
            pl.Series("incomes_operating_1", [float(incomes_operating_1)], dtype=pl.Float64),
            pl.Series("incomes_operating_2", [float(incomes_operating_2)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_1", [float(expenses_salaries_wages_bonus_1)], dtype=pl.Float64),
            pl.Series("expenses_salaries_wages_bonus_2", [float(expenses_salaries_wages_bonus_2)], dtype=pl.Float64),
            pl.Series("expenses_interests_1", [float(expenses_interests_1)], dtype=pl.Float64),
            pl.Series("expenses_interests_2", [float(expenses_interests_2)], dtype=pl.Float64),
            pl.Series("expenses_rent_1", [float(expenses_rent_1)], dtype=pl.Float64),
            pl.Series("expenses_rent_2", [float(expenses_rent_2)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_1", [float(expenses_depreciation_1)], dtype=pl.Float64),
            pl.Series("expenses_depreciation_2", [float(expenses_depreciation_2)], dtype=pl.Float64),
            pl.Series("expenses_donations_1", [float(expenses_donations_1)], dtype=pl.Float64),
            pl.Series("expenses_donations_2", [float(expenses_donations_2)], dtype=pl.Float64),
            pl.Series("expenses_sales_tax_1", [float(expenses_sales_tax_1)], dtype=pl.Float64),
            pl.Series("expenses_sales_tax_2", [float(expenses_sales_tax_2)], dtype=pl.Float64),
            pl.Series("expenses_machinary_equipment_1", [float(expenses_machinary_equipment_1)], dtype=pl.Float64),
            pl.Series("expenses_machinary_equipment_2", [float(expenses_machinary_equipment_2)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_1", [float(expenses_other_purchases_1)], dtype=pl.Float64),
            pl.Series("expenses_other_purchases_2", [float(expenses_other_purchases_2)], dtype=pl.Float64),
            pl.Series("expenses_licenses_1", [float(expenses_licenses_1)], dtype=pl.Float64),
            pl.Series("expenses_licenses_2", [float(expenses_licenses_2)], dtype=pl.Float64),
            pl.Series("expenses_other_operations_1", [float(expenses_other_operations_1)], dtype=pl.Float64),
            pl.Series("expenses_other_operations_2", [float(expenses_other_operations_2)], dtype=pl.Float64),
            pl.Series("expenses_total_1", [float(expenses_total_1)], dtype=pl.Float64),
            pl.Series("expenses_total_2", [float(expenses_total_2)], dtype=pl.Float64),
            pl.Series("gross_profit_1", [float(gross_profit_1)], dtype=pl.Float64),
            pl.Series("gross_profit_2", [float(gross_profit_2)], dtype=pl.Float64),
            pl.Series("profit_income_tax_1", [float(profit_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_income_tax_2", [float(profit_income_tax_2)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_1", [float(profit_after_income_tax_1)], dtype=pl.Float64),
            pl.Series("profit_after_income_tax_2", [float(profit_after_income_tax_2)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_1", [float(sales_tax_withheld_1)], dtype=pl.Float64),
            pl.Series("sales_tax_withheld_2", [float(sales_tax_withheld_2)], dtype=pl.Float64),
            pl.Series("name", [name], dtype=pl.String),
            pl.Series("rank", [rank], dtype=pl.String),
        ]
        
        df = pl.DataFrame(data)
        DAO().insert_forms(df, "IP_530", 40)

        return render(request, "forms/succesfull.html")
    return render(request, "forms/yearly/ingreso_neto/IP-530.html")
