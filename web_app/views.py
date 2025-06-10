import pandas as pd
import os
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from web_app import graphics_function as gf
from .models import *
from src.visualization.income_employment import web_app_income_employment
from src.visualization.product_hts import products_hts
from src.visualization.productos_ranking import productos_ranking
from src.visualization.indice_consumidor import indice_consumidor
from src.visualization.cuestionario_salida import cuestionario_viajero_salida
from src.visualization.cuestionario_viajero import travel_questionaire
from src.visualization.account_settings import account_setting
from src.visualization.add_email import change_email
from src.visualization.indicadores import web_app_indicadores
from src.visualization.macro import web_app_macro
from src.visualization.login import log_in_page 
from src.visualization.imports_exports import web_app_imports_exports
from src.formularios.form_ip_110 import IP_110
from src.formularios.form_jp_304 import JP_304
from src.formularios.form_jp_361 import JP_361
from src.formularios.form_jp_362 import JP_362
from src.formularios.form_jp_364 import JP_364
from src.formularios.form_jp_529 import JP_529
from src.formularios.form_jp_541 import JP_541
from src.formularios.form_jp_363 import JP_363
from src.formularios.form_jp_560_63110 import JP_560_63110
from src.formularios.form_ip_210 import IP_210
from src.formularios.form_ip_220 import IP_220
from src.formularios.form_jp_560_63111 import JP_560_63111
from src.formularios.form_ip_230 import IP_230
from src.formularios.form_jp_560_63210 import JP_560_63210
from src.formularios.form_jp_560_2 import JP_560_2
from src.formularios.form_jp_375 import JP_375
from src.formularios.form_ip_420 import IP_420
from src.formularios.form_ip_480 import IP_480
from src.formularios.form_ip_310 import IP_310
from src.formularios.form_jp_383 import JP_383
from src.formularios.form_ip_440 import IP_440
from src.formularios.form_ip_440g import IP_440g
from src.formularios.form_ip_310b import IP_310b
from src.formularios.form_ip_480a import IP_480a
from src.formularios.form_ip_490 import IP_490
from src.formularios.form_ip_520 import IP_520
from src.formularios.form_jp_536_2 import JP_536_2
from src.formularios.form_ip_510 import IP_510
from src.formularios.form_jp_544 import JP_544
from src.formularios.form_ip_530 import IP_530
from src.formularios.form_ip_520s import IP_520s
from src.formularios.form_ip_520a import IP_520a
from src.formularios.form_ip_230 import IP_230
from src.formularios.form_ip_540 import IP_540
from src.formularios.form_ip_540j import IP_540J
from src.formularios.form_jp_544_2 import JP_544_2
from src.formularios.form_ip_610 import IP_610
from src.formularios.form_ip_710 import IP_710
from src.formularios.form_ip_620 import IP_620
from src.formularios.form_ip_540p import IP_540P
from src.formularios.form_ip_540s import IP_540S
from src.formularios.form_ip_540v import IP_540v
from src.formularios.form_ip_540a import IP_540a
from src.formularios.form_ip_720 import IP_720
from src.formularios.form_ip_810 import IP_810
from src.formularios.form_jp_547 import JP_547
from src.formularios.quaterly.form_jp_361_qrt import JP_361_qrt
from src.formularios.quaterly.form_jp_362_qtr import JP_362_qtr
from src.formularios.quaterly.form_jp_363_qtr import JP_363_qtr
from src.formularios.quaterly.form_jp_364_qtr import JP_364_qtr
from src.formularios.quaterly.form_jp_375_qtr import JP_375_qtr
from src.formularios.quaterly.form_jp_529_qtr import JP_529_qtr
from src.formularios.quaterly.form_jp_536_2_qtr import JP_536_2_qtr
from src.formularios.quaterly.form_jp_544_qtr import JP_544_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_110_qtr import IP_110_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_210_qtr import IP_210_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_220_qtr import IP_220_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_230_qtr import IP_230_qtr

# Formularios Gastos Intangibles
from src.formularios.gastos.form_medicion_ID_archivos_intangibles import Medicion_ID_archivos_intangibles
from src.formularios.gastos.form_medicion_concesiones_recursos_naturales import Medicion_concesiones_recursos_naturales
from src.formularios.gastos.form_medicion_licencias_uso_propiedad_intelectual_marcas_registradas import Medicion_licencias_uso_propiedad_intelectual_o_marcas_registradas
from src.formularios.gastos.form_medicion_gastos_comercializacion_formacion_marca import Medicion_gastos_comercializacion_formacion_marca
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_230_qtr import IP_230_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_230_qtr import IP_230_qtr
from src.formularios.quaterly.ingreso_neto_qtr.form_ip_230_qtr import IP_230_qtr

from src.data.proyecciones import *
from src.data.demografic import *
from src.data.idh import *
from src.visualization.cuestionario_viajero_english import cuestionario_viajero_english
from src.visualization.cuestionario_viajero_spanish import cuestionario_viajero_spanish
from src.formularios.form_jp_480 import JP_480

def home(request):
    return render(request, "home.html")

def proyectos(request):
    return render(request, "proyectos.html")

def colaboradores(request):
    return render(request, "colaboradores.html")

def macro(request):
    return web_app_macro(request)
  
def imports_and_exports(request):
    return web_app_imports_exports(request)

def indice_desarrollo_humano(request):
    # Generate the idh index graphs
    normal_graph_html =  normal_indexes_graph()
    adjusted_graph_html = adjusted_indexes_graph()
    
    context = {
        "graph_html": normal_graph_html,
        "adjusted_graph_html": adjusted_graph_html,
    }
    
    return render(request, "indice_desarrollo_humano.html", context)

# Generate the IDH index CSV file response
def idh_index_csv(request):
    file_path = os.path.join(settings.BASE_DIR, "data", "processed", "idh_index.csv")
    return FileResponse(open(file_path, "rb"),
                        as_attachment=True,
                        filename="idh_index.csv",
                        content_type="text/csv")

def datos_demograficos(request):
    # Generate the annual demographic graph
    graph_html = demographic_graph()
    t_graph_html = trimestral_demographic_graph()
    m_graph_html = monthly_demographic_graph()
    d_table = demographic_table(request)
    f_graph_html = fiscal_demographic_graph()

    context = {
        "graph": graph_html,
        "t_graph": t_graph_html,
        "m_graph": m_graph_html,
        "d_table": d_table,
        "f_graph": f_graph_html
    }

    return render(request, "demograficos.html", context)

def ciclos_economicos(request):
    x = [
        2000,
        2001,
        2002,
        2003,
        2004,
        2005,
        2006,
        2007,
        2008,
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024,
    ]
    y = [
        14,
        55,
        44,
        13,
        29,
        20,
        45,
        39,
        29,
        10,
        50,
        60,
        39,
        36,
        49,
        18,
        49,
        50,
        69,
        18,
        13,
        11,
        4,
        2,
        1,
    ]

    x_title = ""
    y_title = ""

    fig = gf.graph(x, y, x_title, y_title)

    ciclos_economicos = fig.to_html()

    context = {"ciclos_economicos": ciclos_economicos}
    return render(request, "ciclos_economicos.html", context)

def indicadores(request):
    return web_app_indicadores(request)

def succesfull_page(request):
    return render(request, "forms/succesfull.html")

# @login_required(login_url='web_app:log_in_page')
def Forms(request):
    user = request.user
    return render(request, "forms/forms.html", {"user": user})

def JP_544_1(request):
    return render(request, "forms/yearly/balanza_de_pagos/JP-544-1.html")

def logout_view(request):
    logout(request)
    return redirect('web_app:log_in_page')
