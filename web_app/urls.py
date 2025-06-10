from django.contrib import admin
from django.urls import path, re_path
from web_app import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

app_name = 'web_app'

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^proyectos/$", views.proyectos, name="proyectos"),
    re_path(r"^colaboradores/$", views.colaboradores, name="colaboradores"),
    re_path(r"^proyecciones/$", views.proyecciones_poblacionales, name="proyecciones_poblacionales"),
    re_path(r"^centro-de-datos-macroeconomicos/$", views.macro, name="macro"),
    re_path(r"^indice-desarrollo-humano/$", views.indice_desarrollo_humano, name="indice-desarrollo-humano"),
    re_path(r"^ciclos-economicos/$", views.ciclos_economicos, name="ciclos_economicos"),
    re_path(r"^indicadores-mensuales/$", views.indicadores, name="indicadores"),
    re_path(r"^datos-demograficos/$", views.datos_demograficos, name="datos_demograficos"),
    re_path(r"^succesfull_page/$", views.succesfull_page, name="succesfull_page"),
    re_path(r"^JP-304-relacion-de-aportaciones-federales/$", views.JP_304, name="JP-304"),
    re_path(r"^IP-110-agricultura/$", views.IP_110, name="IP-110"),
    re_path(r"^JP-541-valor-de-la-inversion-en-obras-de-construccion/$", views.JP_541, name="JP-541"),
    re_path(r"^JP-361-transactions-in-pr-of-external-insurance-companies/$", views.JP_361, name="JP-361"),
    re_path(r"^JP-362-transacciones-con-el-exterior/$", views.JP_362, name="JP-362"),
    re_path(r"^JP-363-investment-in-securities-of-the-central-goverment/$", views.JP_363, name="JP-363"),
    re_path(r"^JP-560-63110-seguros-domesticos-de-vida/$", views.JP_560_63110, name="JP-560-63110"),
    re_path(r"^IP-210-mineria/$", views.IP_210, name="IP-210"),    
    re_path(r"^IP-220-utilidades/$", views.IP_220, name="IP-220"),
    re_path(r"^IP-230-construccion/$", views.IP_230, name="IP-230"),
    re_path(r"^IP-310-manufactura/$", views.IP_310, name="IP-310"),
    re_path(r"^JP-560-63111-organizaciones-de-servicio-de-salud/$", views.JP_560_63111, name="JP-560-63111"),
    re_path(r"^JP-560-63210-seguros-domesticos-propiedad-contingencia/$", views.JP_560_63210, name="JP-560-63210"),
    re_path(r"^JP-364-informacion-sobre-compañias de seguros/$", views.JP_364, name="JP-364"),
    re_path(r"^JP-375-encuesta-sobre-valor-pendinente/$", views.JP_375, name="JP-375"),
    re_path(r"^JP-362-transacciones-con-el-exterior-para-la-balanza/$", views.JP_362, name="JP-362"),
    re_path(r"^JP-560-2-preliminar/$", views.JP_560_2, name="JP-560-2"),
    re_path(r"^JP-383-pagos-de-asistencia/$", views.JP_383, name="JP-383"),
    re_path(r"^IP-480-transportacion/$", views.IP_480, name="IP-480"),
    re_path(r"^IP-420-comercio-al-por-mayor/$", views.IP_420, name="IP-420"),
    re_path(r"^IP-440-comercio-al-detal/$", views.IP_440, name="IP-440"),
    re_path(r"^IP-440g-estaciones-de-gasolina/$", views.IP_440g, name="IP-440g"),
    re_path(r"^IP-310b-manufacturas-de-bebidas/$", views.IP_310b, name="IP-310b"),
    re_path(r"^IP-480a-transportacion-aerea/$", views.IP_480a, name="IP-480a"),
    re_path(r"^JP-529-relacion-de-aportaciones/$", views.JP_529, name="JP-529"),
    re_path(r"^IP-490-correos-y-mensajeros/$", views.IP_490, name="IP-490"),
    re_path(r"^IP-520-finanzas-y-seguros/$", views.IP_520, name="IP-520"),
    re_path(r"^JP-536-2-producto-bruto/$", views.JP_536_2, name="JP-536-2"),
    re_path(r"^IP-510-informatica/$", views.IP_510, name="IP-510"),
    re_path(r"^JP-544-info-para-balanza/$", views.JP_544, name="JP-544"),
    re_path(r"^JP-544-1-instrucciones/$", views.JP_544_1, name="JP-544-1"),
    re_path(r"^IP-520a-agencias-corretaje-y-otros/$", views.IP_520a, name="IP-520a"),
    re_path(r"^IP-520s-empresas-aseguradoras-y-actividades-relacionadas/$", views.IP_520s, name="IP-520s"),
    re_path(r"^IP-530-inmobiliaria-y-arrendamientos/$", views.IP_530, name="IP-530"),
    re_path(r"^IP-540-servicios-profesionales-tecnicos-y-cientificos/$", views.IP_540, name="IP-540"),
    re_path(r"^IP-540P-organizacion-de-viajes-y-servicios-de-reservacion/$", views.IP_540P, name="IP-540P"),
    re_path(r"^IP-540J-administracion-de-empresas/$", views.IP_540J, name="IP-540J"),
    re_path(r"^JP-544-2-aportaciones-federales/$", views.JP_544_2, name="JP-544-2"),
    re_path(r"^IP-610-servicios-de-educacion/$", views.IP_610, name="IP-610"),
    re_path(r"^IP-710-arte-entretenimiento-y-recreacion/$", views.IP_710, name="IP-710"),
    re_path(r"^IP-620-servicios-de-salud/$", views.IP_620, name="IP-620"),
    re_path(r"^IP-540S-servicios-administrativos-y-de-apoyo/$", views.IP_540S, name="IP-540S"),
    re_path(r"^IP-540a-publicidad-y-servicios-relacionados/$", views.IP_540a, name="IP-540a"),
    re_path(r"^IP-540v-veterinarios-y-otros-servicios-de-animales/$", views.IP_540v, name="IP-540v"),
    re_path(r"^IP-720-alojamiento-y-servicio-de-comida/$", views.IP_720, name="IP-720"),
    re_path(r"^IP-810-otros-servicios/$", views.IP_810, name="IP-810"),
    re_path(r"^JP-547-agencies-transactions/$", views.JP_547, name="JP-547"),
    re_path(r"^transacciones-foraneas/$", views.imports_and_exports, name="imports-and-exports"),
    re_path(r"^forms/$", views.Forms, name="forms"), 
    re_path(r"^log-in-page/$", LoginView.as_view(template_name='registration/login.html'), name='log_in_page'),
    re_path(r"^logout/", views.logout_view, name='logout'),
    re_path(r"^add-email/$", views.change_email, name='add_email'),
    re_path(r"^account-settings/$", views.account_setting, name='account_settings'),
    re_path(r"^productos-hts/$", views.products_hts, name='product_hts'),
    re_path(r"^productos_ranking/$", views.productos_ranking, name='productos_ranking'),
    re_path(r"^ingresos-de-empleos/$", views.web_app_income_employment, name='income_employment'),
    re_path(r"^indice-al-consumidor/$", views.indice_consumidor, name='indice_consumidor'),
    re_path(r"^awards/$", views.awards, name='awards'),

    re_path(r"^cuestionario-del-viajero/$", views.travel_questionaire, name='travel_questionaire'),
    re_path(r"^cuestionario-del-viajero-english/$", views.cuestionario_viajero_english, name='cuestionario_viajero_english'),
    re_path(r"^cuestionario-del-viajero-spanish/$", views.cuestionario_viajero_spanish, name='cuestionario_viajero_spanish'),
    re_path(r"^cuestionario-del-viajero-salida/$", views.cuestionario_viajero_salida, name='cuestionario_viajero_salida'),


        
    # Asegura los path que estén bien cuando añadas otro
    re_path(r"^JP-361-transactions-in-pr-of-external-insurance-companies-qrt/$", views.JP_361_qrt, name="JP-361-qrt"),
    re_path(r"^JP-362-transacciones-con-el-exterior-para-la-balanza-de-Puerto-Rico-qtr/$", views.JP_362_qtr, name="JP-362-qtr"),
    re_path(r"^JP-363-investment-in-securities-of-the-central-goverment-qtr/$", views.JP_363_qtr, name="JP-363-qtr"),
    re_path(r"^JP-364-informacion-sobre-compañias-de-seguros-qtr/$", views.JP_364_qtr, name="JP-364-qtr"),
    re_path(r"^JP-375-encuesta-sobre-valor-pendinente-qtr/$", views.JP_375_qtr, name="JP-375-qtr"),
    re_path(r"^JP-529-relacion-de-aportaciones-qtr/$", views.JP_529_qtr, name="JP-529-qtr"),
    re_path(r"^JP-536-2-producto-bruto-qtr/$", views.JP_536_2_qtr, name="JP-536-2-qtr"),
    re_path(r"^JP-544-info-para-balanza-qtr/$", views.JP_544_qtr, name="JP-544-qtr"),
    re_path(r"^IP-110-agricultura-qtr/$", views.IP_110_qtr, name="IP-110-qtr"),
    re_path(r"^IP-210-mineria-qtr/$", views.IP_210_qtr, name="IP-210-qtr"),    
    re_path(r"^IP-220-utilidades-qtr/$", views.IP_220_qtr, name="IP-220_qtr"),
    re_path(r"^IP-230-construccion-qtr/$", views.IP_230_qtr, name="IP-230-qtr"),

    re_path(r"^idh-index/csv/$", views.idh_index_csv, name="idh_index_csv"),    # for IDH index CSV download
    
    # Gastos intangibles
    
    re_path(r"^medicion-activos-ID-en-activos-intangibles/$", views.Medicion_ID_archivos_intangibles, name="Medicion-ID-archivos-intangibles"),
    re_path(r"^concesiones-recursos-naturales-activos-intangibles/$", views.Medicion_concesiones_recursos_naturales, name="Medicion-concesiones-recursos-naturales"),
    re_path(r"^medicion-licencias-propiedad-intelectual-marcas-registradas/$", views.Medicion_licencias_uso_propiedad_intelectual_o_marcas_registradas, name="medicion-licencias-propiedad-intelectual-marcas-registradas"),
    re_path(r"^medicion-gastos-comercializacion-formacion-marca/$", views.Medicion_gastos_comercializacion_formacion_marca, name="medicion-gastos-comercializacion-formacion-marca"),
    re_path(r"^medicion-productos-entretenimiento-activos-intangibles/$", views.IP_230_qtr, name="IP-230-qtr"),
    re_path(r"^medicion-software-bases-de-datos-activos-intangibles/$", views.IP_230_qtr, name="IP-230-qtr"),
    re_path(r"^gastos-comercialización-y-formacion-marca/$", views.JP_480, name="JP-480"),
    
    
]

