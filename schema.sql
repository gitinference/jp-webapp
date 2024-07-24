-- MASTER TABLE --
CREATE TABLE Forms {
  id INTEGER,
  name TEXT NOT NULL,
  PRIMARY KEY (id)
}


-- CONSTRUCTION --
CREATE TABLE JP_541 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}


--BALANZA DE PAGOS --
CREATE TABLE JP_304 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_361 {
  id INTEGER,
  form_id INTEGER,
  income_expenses_year_1 INTEGER NOT NULL,
  income_expenses_year_2 INTEGER NOT NULL,
  income_life_1 NUMERIC NOT NULL,
  income_life_2 NUMERIC NOT NULL,
  income_disability_1 NUMERIC NOT NULL,
  income_disability_2 NUMERIC NOT NULL,
  income_auto_1 NUMERIC NOT NULL,
  income_auto_2 NUMERIC NOT NULL,
  income_other_1 NUMERIC NOT NULL,
  income_other_2 NUMERIC NOT NULL,
  income_interest_1 NUMERIC NOT NULL,
  income_interest_2 NUMERIC NOT NULL,
  income_rent_1 NUMERIC NOT NULL,
  income_rent_2 NUMERIC NOT NULL,
  income_other_2_1 NUMERIC NOT NULL,
  income_other_2_2 NUMERIC NOT NULL,
  total_income_1 NUMERIC NOT NULL,
  total_income_2 NUMERIC NOT NULL,
  expenses_life_1 NUMERIC NOT NULL,
  expenses_life_2 NUMERIC NOT NULL,
  expenses_disability_1 NUMERIC NOT NULL,
  expenses_disability_2 NUMERIC NOT NULL,
  expenses_auto_1 NUMERIC NOT NULL,
  expenses_auto_2 NUMERIC NOT NULL,
  expenses_other_1 NUMERIC NOT NULL,
  expenses_other_2 NUMERIC NOT NULL,
  expenses_salaries_1 NUMERIC NOT NULL,
  expenses_salaries_2 NUMERIC NOT NULL,
  expenses_interes_1 NUMERIC NOT NULL,
  expenses_interes_2 NUMERIC NOT NULL,
  expenses_rent_1 NUMERIC NOT NULL,
  expenses_rent_2 NUMERIC NOT NULL,
  expenses_depreciation_1 NUMERIC NOT NULL,
  expenses_depreciation_2 NUMERIC NOT NULL,
  expenses_donations_1 NUMERIC NOT NULL,
  expenses_donations_2 NUMERIC NOT NULL,
  expenses_commissions_1 NUMERIC NOT NULL,
  expenses_commissions_2 NUMERIC NOT NULL,
  expenses_employees_1 NUMERIC NOT NULL,
  expenses_employees_2 NUMERIC NOT NULL,
  expenses_brokers_1 NUMERIC NOT NULL,
  expenses_brokers_2 NUMERIC NOT NULL,
  expenses_other_operational_1 NUMERIC NOT NULL,
  expenses_other_operational_2 NUMERIC NOT NULL,
  total_expenses_1 NUMERIC NOT NULL,
  total_expenses_2 NUMERIC NOT NULL,
  net_profit_1 NUMERIC NOT NULL,
  net_profit_2 NUMERIC NOT NULL,
  balance_year_1 INTEGER NOT NULL,
  balance_year_2 INTEGER NOT NULL,
  guaranteed_1 NUMERIC NOT NULL,
  guaranteed_2 NUMERIC NOT NULL,
  guaranteed_3 NUMERIC NOT NULL,
  guaranteed_4 NUMERIC NOT NULL,
  veterans_1 NUMERIC NOT NULL,
  veterans_2 NUMERIC NOT NULL,
  veterans_3 NUMERIC NOT NULL,
  veterans_4 NUMERIC NOT NULL,
  conventional_1 NUMERIC NOT NULL,
  conventional_2 NUMERIC NOT NULL,
  conventional_3 NUMERIC NOT NULL,
  conventional_4 NUMERIC NOT NULL,
  other_1 NUMERIC NOT NULL,
  other_2 NUMERIC NOT NULL,
  other_3 NUMERIC NOT NULL,
  other_4 NUMERIC NOT NULL,
  policy_loans_1 NUMERIC NOT NULL,
  policy_loans_2 NUMERIC NOT NULL,
  policy_loans_3 NUMERIC NOT NULL,
  policy_loans_4 NUMERIC NOT NULL,
  other_specify_1 NUMERIC NOT NULL,
  other_specify_2 NUMERIC NOT NULL,
  other_specify_3 NUMERIC NOT NULL,
  other_specify_4 NUMERIC NOT NULL,
  policy_reserves_1 NUMERIC NOT NULL,
  policy_reserves_2 NUMERIC NOT NULL,
  accrued_dividends_1 NUMERIC NOT NULL,
  accrued_dividends_2 NUMERIC NOT NULL,
  signature TEXT NOT NULL,
  date TEXT NOT NULL,
  phone TEXT NOT NULL,
  position TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_362 {
  id INTEGER,
  form_id INTEGER,

  year_1 INTEGER NOT NULL,
  year_2 INTEGER NOT NULL,
  company_name TEXT NOT NULL,

  debts_balance NUMERIC NOT NULL,
  debts_emision NUMERIC NOT NULL,
  debts_amortizacion NUMERIC NOT NULL,
  debts_final NUMERIC NOT NULL,
  debts_interes NUMERIC NOT NULL,
  debts_acreedor NUMERIC NOT NULL,

  debts_bond_balance NUMERIC NOT NULL,
  debts_bond_emision NUMERIC NOT NULL,
  debts_bond_amortizacion NUMERIC NOT NULL,
  debts_bond_final NUMERIC NOT NULL,
  debts_bond_interes NUMERIC NOT NULL,
  debts_bond_acreedor NUMERIC NOT NULL,

  debts_promossory_notes_balance NUMERIC NOT NULL,
  debts_promossory_notes_emision NUMERIC NOT NULL,
  debts_promossory_notes_amortizacion NUMERIC NOT NULL,
  debts_promossory_notes_final NUMERIC NOT NULL,
  debts_promossory_notes_interes NUMERIC NOT NULL,
  debts_promossory_notes_acreedor NUMERIC NOT NULL,

  debts_others_balance NUMERIC NOT NULL,
  debts_others_emision NUMERIC NOT NULL,
  debts_others_amortizacion NUMERIC NOT NULL,
  debts_others_final NUMERIC NOT NULL,
  debts_others_interes NUMERIC NOT NULL,
  debts_others_acreedor NUMERIC NOT NULL,

  short_promossory_balance NUMERIC NOT NULL,
  short_promossory_emision NUMERIC NOT NULL,
  short_promossory_amortizacion NUMERIC NOT NULL,
  short_promossory_final NUMERIC NOT NULL,
  short_promossory_interes NUMERIC NOT NULL,
  short_promossory_acreedor NUMERIC NOT NULL,

  short_account_balance NUMERIC NOT NULL,
  short_account_emision NUMERIC NOT NULL,
  short_account_amortizacion NUMERIC NOT NULL,
  short_account_final NUMERIC NOT NULL,
  short_account_interes NUMERIC NOT NULL,
  short_account_acreedor NUMERIC NOT NULL,

  short_others_balance NUMERIC NOT NULL,
  short_others_emision NUMERIC NOT NULL,
  short_others_amortizacion NUMERIC NOT NULL,
  short_others_final NUMERIC NOT NULL,
  short_others_interes NUMERIC NOT NULL,
  short_others_acreedor NUMERIC NOT NULL,

  short_term_balance NUMERIC NOT NULL,
  short_term_emision NUMERIC NOT NULL,
  short_term_amortizacion NUMERIC NOT NULL,
  short_term_final NUMERIC NOT NULL,
  short_term_interes NUMERIC NOT NULL,
  short_term_acreedor NUMERIC NOT NULL,

  assets_balance NUMERIC NOT NULL,
  assets_emision NUMERIC NOT NULL,
  assets_amortizacion NUMERIC NOT NULL,
  assets_final NUMERIC NOT NULL,
  assets_interes NUMERIC NOT NULL,

  assets_values_balance NUMERIC NOT NULL,
  assets_values_emision NUMERIC NOT NULL,
  assets_values_amortizacion NUMERIC NOT NULL,
  assets_values_final NUMERIC NOT NULL,
  assets_values_interes NUMERIC NOT NULL,

  assets_others_balance NUMERIC NOT NULL,
  assets_others_emision NUMERIC NOT NULL,
  assets_others_amortizacion NUMERIC NOT NULL,
  assets_others_final NUMERIC NOT NULL,
  assets_others_interes NUMERIC NOT NULL,

  short_balance NUMERIC NOT NULL,
  short_emision NUMERIC NOT NULL,
  short_amortizacion NUMERIC NOT NULL,
  short_final NUMERIC NOT NULL,
  short_interes NUMERIC NOT NULL,

  short_balance_balance NUMERIC NOT NULL,
  short_balance_emision NUMERIC NOT NULL,
  short_balance_amortizacion NUMERIC NOT NULL,
  short_balance_final NUMERIC NOT NULL,
  short_balance_interes NUMERIC NOT NULL,

  short_accouts_balance NUMERIC NOT NULL,
  short_accouts_emision NUMERIC NOT NULL,
  short_accouts_amortizacion NUMERIC NOT NULL,
  short_accouts_final NUMERIC NOT NULL,
  short_accouts_interes NUMERIC NOT NULL,

  short_others_balance_2 NUMERIC NOT NULL,
  short_others_emision_2 NUMERIC NOT NULL,
  short_others_amortizacion_2 NUMERIC NOT NULL,
  short_others_final_2 NUMERIC NOT NULL,
  short_others_interes_2 NUMERIC NOT NULL,

  signature TEXT NOT NULL,
  position TEXT NOT NULL,
  date TEXT NOT NULL,
  phone TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_363 {
  id INTEGER,
  form_id INTEGER,

  bonds_year_left INTEGER NOT NULL,
  bonds_year_right INTEGER NOT NULL,
  notes_year_left INTEGER NOT NULL,
  notes_year_right INTEGER NOT NULL,

  town_bonds_left NUMERIC NOT NULL,
  town_bonds_right NUMERIC NOT NULL,
  town_notes_left NUMERIC NOT NULL,
  town_notes_right NUMERIC NOT NULL,
  town_name_service TEXT NOT NULL,

  PC_bonds_left NUMERIC NOT NULL,
  PC_bonds_right NUMERIC NOT NULL,
  PC_notes_left NUMERIC NOT NULL,
  PC_notes_right NUMERIC NOT NULL,
  PC_name_service TEXT NOT NULL,

  EPA_bonds_left NUMERIC NOT NULL,
  EPA_bonds_right NUMERIC NOT NULL,
  EPA_notes_left NUMERIC NOT NULL,
  EPA_notes_right NUMERIC NOT NULL,
  EPA_name_service TEXT NOT NULL,

  HA_bonds_left NUMERIC NOT NULL,
  HA_bonds_right NUMERIC NOT NULL,
  HA_notes_left NUMERIC NOT NULL,
  HA_notes_right NUMERIC NOT NULL,
  HA_name_service TEXT NOT NULL,

  ASA_bonds_left NUMERIC NOT NULL,
  ASA_bonds_right NUMERIC NOT NULL,
  ASA_notes_left NUMERIC NOT NULL,
  ASA_notes_right NUMERIC NOT NULL,
  ASA_name_service TEXT NOT NULL,

  PBA_bonds_left NUMERIC NOT NULL,
  PBA_bonds_right NUMERIC NOT NULL,
  PBA_notes_left NUMERIC NOT NULL,
  PBA_notes_right NUMERIC NOT NULL,
  PBA_name_service TEXT NOT NULL,

  PA_bonds_left NUMERIC NOT NULL,
  PA_bonds_right NUMERIC NOT NULL,
  PA_notes_left NUMERIC NOT NULL,
  PA_notes_right NUMERIC NOT NULL,
  PA_name_service TEXT NOT NULL,

  IDC_bonds_left NUMERIC NOT NULL,
  IDC_bonds_right NUMERIC NOT NULL,
  IDC_notes_left NUMERIC NOT NULL,
  IDC_notes_right NUMERIC NOT NULL,
  IDC_name_service TEXT NOT NULL,

  GDB_bonds_left NUMERIC NOT NULL,
  GDB_bonds_right NUMERIC NOT NULL,
  GDB_notes_left NUMERIC NOT NULL,
  GDB_notes_right NUMERIC NOT NULL,
  GDB_name_service TEXT NOT NULL,

  HFC_bonds_left NUMERIC NOT NULL,
  HFC_bonds_right NUMERIC NOT NULL,
  HFC_notes_left NUMERIC NOT NULL,
  HFC_notes_right NUMERIC NOT NULL,
  HFC_name_service TEXT NOT NULL,

  other TEXT NOT NULL,
  other_bonds_left NUMERIC NOT NULL,
  other_bonds_right NUMERIC NOT NULL,
  other_notes_left NUMERIC NOT NULL,
  other_notes_right NUMERIC NOT NULL,
  other_name_service TEXT NOT NULL,

  other_PC_1 TEXT NOT NULL,
  other_PC_1_bonds_left NUMERIC NOT NULL,
  other_PC_1_bonds_right NUMERIC NOT NULL,
  other_PC_1_notes_left NUMERIC NOT NULL,
  other_PC_1_notes_right NUMERIC NOT NULL,
  other_PC_1_name_service TEXT NOT NULL,

  other_PC_2 TEXT NOT NULL,
  other_PC_2_bonds_left NUMERIC NOT NULL,
  other_PC_2_bonds_right NUMERIC NOT NULL,
  other_PC_2_notes_left NUMERIC NOT NULL,
  other_PC_2_notes_right NUMERIC NOT NULL,
  other_PC_2_name_service TEXT NOT NULL,

  GNMA_bonds_left NUMERIC NOT NULL,
  GNMA_bonds_right NUMERIC NOT NULL,
  GNMA_notes_left NUMERIC NOT NULL,
  GNMA_notes_right NUMERIC NOT NULL,
  GNMA_name_service TEXT NOT NULL,

  other5 TEXT NOT NULL,
  other5_bonds_left NUMERIC NOT NULL,
  other5_bonds_right NUMERIC NOT NULL,
  other5_notes_left NUMERIC NOT NULL,
  other5_notes_right NUMERIC NOT NULL,
  other5_name_service TEXT NOT NULL,

  signature TEXT NOT NULL,
  position TEXT NOT NULL,
  date TEXT NOT NULL,
  phone TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_364 {
  id INTEGER,
  form_id INTEGER,

  year_bono1 INTEGER NOT NULL,
  year_bono2 INTEGER NOT NULL,
  year_paga1 INTEGER NOT NULL,
  year_paga2 INTEGER NOT NULL,

  ELA_bono1 NUMERIC NOT NULL,
  ELA_bono2 NUMERIC NOT NULL,
  ELA_paga1 NUMERIC NOT NULL,
  ELA_paga2 NUMERIC NOT NULL,
  ELA_agente TEXT NOT NULL,
  
  municipio_bono1 NUMERIC NOT NULL,
  municipio_bono2 NUMERIC NOT NULL,
  municipio_paga1 NUMERIC NOT NULL,
  municipio_paga2 NUMERIC NOT NULL,
  municipio_agente TEXT NOT NULL,
  
  corp_publicas_bono1 NUMERIC NOT NULL,
  corp_publicas_bono2 NUMERIC NOT NULL,
  corp_publicas_paga1 NUMERIC NOT NULL,
  corp_publicas_paga2 NUMERIC NOT NULL,
  corp_publicas_agente TEXT NOT NULL,
  
  AEE_bono1 NUMERIC NOT NULL,
  AEE_bono2 NUMERIC NOT NULL,
  AEE_paga1 NUMERIC NOT NULL,
  AEE_paga2 NUMERIC NOT NULL,
  AEE_agente TEXT NOT NULL,
  
  Acarreteras_bono1 NUMERIC NOT NULL,
  Acarreteras_bono2 NUMERIC NOT NULL,
  Acarreteras_paga1 NUMERIC NOT NULL,
  Acarreteras_paga2 NUMERIC NOT NULL,
  Acarreteras_agente TEXT NOT NULL,
  
  AAA_bono1 NUMERIC NOT NULL,
  AAA_bono2 NUMERIC NOT NULL,
  AAA_paga1 NUMERIC NOT NULL,
  AAA_paga2 NUMERIC NOT NULL,
  AAA_agente TEXT NOT NULL,
  
  AEP_bono1 NUMERIC NOT NULL,
  AEP_bono2 NUMERIC NOT NULL,
  AEP_paga1 NUMERIC NOT NULL,
  AEP_paga2 NUMERIC NOT NULL,
  AEP_agente TEXT NOT NULL,
  
  AP_bono1 NUMERIC NOT NULL,
  AP_bono2 NUMERIC NOT NULL,
  AP_paga1 NUMERIC NOT NULL,
  AP_paga2 NUMERIC NOT NULL,
  AP_agente TEXT NOT NULL,
  
  AT_bono1 NUMERIC NOT NULL,
  AT_bono2 NUMERIC NOT NULL,
  AT_paga1 NUMERIC NOT NULL,
  AT_paga2 NUMERIC NOT NULL,
  AT_agente TEXT NOT NULL,
  
  CFI_bono1 NUMERIC NOT NULL,
  CFI_bono2 NUMERIC NOT NULL,
  CFI_paga1 NUMERIC NOT NULL,
  CFI_paga2 NUMERIC NOT NULL,
  CFI_agente TEXT NOT NULL,
  
  BGF_bono1 NUMERIC NOT NULL,
  BGF_bono2 NUMERIC NOT NULL,
  BGF_paga1 NUMERIC NOT NULL,
  BGF_paga2 NUMERIC NOT NULL,
  BGF_agente TEXT NOT NULL,
  
  CFV_bono1 NUMERIC NOT NULL,
  CFV_bono2 NUMERIC NOT NULL,
  CFV_paga1 NUMERIC NOT NULL,
  CFV_paga2 NUMERIC NOT NULL,
  CFV_agente TEXT NOT NULL,
  
  otherk_title TEXT NOT NULL,
  otherk_bono1 NUMERIC NOT NULL,
  otherk_bono2 NUMERIC NOT NULL,
  otherk_paga1 NUMERIC NOT NULL,
  otherk_paga2 NUMERIC NOT NULL,
  otherk_agente TEXT NOT NULL,
  
  otherl_title TEXT NOT NULL,
  otherl_bono1 NUMERIC NOT NULL,
  otherl_bono2 NUMERIC NOT NULL,
  otherl_paga1 NUMERIC NOT NULL,
  otherl_paga2 NUMERIC NOT NULL,
  otherl_agente TEXT NOT NULL,
  
  otherm_title TEXT NOT NULL,
  otherm_bono1 NUMERIC NOT NULL,
  otherm_bono2 NUMERIC NOT NULL,
  otherm_paga1 NUMERIC NOT NULL,
  otherm_paga2 NUMERIC NOT NULL,
  otherm_agente TEXT NOT NULL,
  
  year_balance1 INTEGER NOT NULL,
  year_balance2 INTEGER NOT NULL,
  
  FHA_balance1 NUMERIC NOT NULL,
  FHA_balance2 NUMERIC NOT NULL,
  FHA_agente TEXT NOT NULL,
  
  GAV_balance1 NUMERIC NOT NULL,
  GAV_balance2 NUMERIC NOT NULL,
  GAV_agente TEXT NOT NULL,
  
  convencionales_balance1 NUMERIC NOT NULL,
  convencionales_balance2 NUMERIC NOT NULL,
  convencionales_agente TEXT NOT NULL,
  
  otras_instituciones_balance1 NUMERIC NOT NULL,
  otras_instituciones_balance2 NUMERIC NOT NULL,
  otras_instituciones_agente TEXT NOT NULL,
  
  prestamos_hipo_balance1 NUMERIC NOT NULL,
  prestamos_hipo_balance2 NUMERIC NOT NULL,
  prestamos_hipo_agente TEXT NOT NULL,
  
  prestamos_comerciales_industriales_balance1 NUMERIC NOT NULL,
  prestamos_comerciales_industriales_balance2 NUMERIC NOT NULL,
  prestamos_comerciales_industriales_agente TEXT NOT NULL,
  
  prestamos_poliza_balance1 NUMERIC NOT NULL,
  prestamos_poliza_balance2 NUMERIC NOT NULL,
  prestamos_poliza_agente TEXT NOT NULL,
  
  reservas_poliza_balance1 NUMERIC NOT NULL,
  reservas_poliza_balance2 NUMERIC NOT NULL,
  reservas_poliza_agente TEXT NOT NULL,
  
  dividendos_poliza_balance1 NUMERIC NOT NULL,
  dividendos_poliza_balance2 NUMERIC NOT NULL,
  dividendos_poliza_agente TEXT NOT NULL,

  signature TEXT NOT NULL,
  phone TEXT NOT NULL,
  nombre_persona TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_375 {
  id INTEGER,
  form_id INTEGER,

  year_1 INTEGER NOT NULL,
  year_2 INTEGER NOT NULL,
  year_3 INTEGER NOT NULL,

  FHA_1 NUMERIC NOT NULL,
  FHA_2 NUMERIC NOT NULL,
  FHA_3 NUMERIC NOT NULL,
  veteran_1 NUMERIC NOT NULL,
  veteran_2 NUMERIC NOT NULL,
  veteran_3 NUMERIC NOT NULL,
  bank_1 NUMERIC NOT NULL,
  bank_2 NUMERIC NOT NULL,
  bank_3 NUMERIC NOT NULL,
  conventional_1 NUMERIC NOT NULL,
  conventional_2 NUMERIC NOT NULL,
  conventional_3 NUMERIC NOT NULL,
  other_1 NUMERIC NOT NULL,
  other_2 NUMERIC NOT NULL,
  other_3 NUMERIC NOT NULL,
  
  FHA_2_1 NUMERIC NOT NULL,
  FHA_2_2 NUMERIC NOT NULL,
  FHA_2_3 NUMERIC NOT NULL,
  veteran_2_1 NUMERIC NOT NULL,
  veteran_2_2 NUMERIC NOT NULL,
  veteran_2_3 NUMERIC NOT NULL,
  conventional_2_1 NUMERIC NOT NULL,
  conventional_2_2 NUMERIC NOT NULL,
  conventional_2_3 NUMERIC NOT NULL,
  others_2_1 NUMERIC NOT NULL,
  others_2_2 NUMERIC NOT NULL,
  others_2_3 NUMERIC NOT NULL,
  
  FHA_3_1 NUMERIC NOT NULL,
  FHA_3_2 NUMERIC NOT NULL,
  FHA_3_3 NUMERIC NOT NULL,
  veteran_3_1 NUMERIC NOT NULL,
  veteran_3_2 NUMERIC NOT NULL,
  veteran_3_3 NUMERIC NOT NULL,
  bank_2_1 NUMERIC NOT NULL,
  bank_2_2 NUMERIC NOT NULL,
  bank_2_3 NUMERIC NOT NULL,
  conventional_3_1 NUMERIC NOT NULL,
  conventional_3_2 NUMERIC NOT NULL,
  conventional_3_3 NUMERIC NOT NULL,
  others_3_1 NUMERIC NOT NULL,
  others_3_2 NUMERIC NOT NULL,
  others_3_3 NUMERIC NOT NULL,
  
  FHA_4_1 NUMERIC NOT NULL,
  FHA_4_2 NUMERIC NOT NULL,
  FHA_4_3 NUMERIC NOT NULL,
  veteran_4_1 NUMERIC NOT NULL,
  veteran_4_2 NUMERIC NOT NULL,
  veteran_4_3 NUMERIC NOT NULL,
  conventional_4_1 NUMERIC NOT NULL,
  conventional_4_2 NUMERIC NOT NULL,
  conventional_4_3 NUMERIC NOT NULL,
  others_4_1 NUMERIC NOT NULL,
  others_4_2 NUMERIC NOT NULL,
  others_4_3 NUMERIC NOT NULL,
  
  commissions_1 NUMERIC NOT NULL,
  commissions_2 NUMERIC NOT NULL,
  commissions_3 NUMERIC NOT NULL,

  phone TEXT NOT NULL,
  signature TEXT NOT NULL,
  position TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_383 {
  id INTEGER,
  form_id INTEGER,

  other_section TEXT NOT NULL,
  año INTEGER NOT NULL,
  julio_1 NUMERIC NOT NULL,
  julio_2 NUMERIC NOT NULL,
  julio_3 NUMERIC NOT NULL,
  julio_4 NUMERIC NOT NULL,
  julio_5 NUMERIC NOT NULL,
  julio_6 NUMERIC NOT NULL,
  agosto_1 NUMERIC NOT NULL,
  agosto_2 NUMERIC NOT NULL,
  agosto_3 NUMERIC NOT NULL,
  agosto_4 NUMERIC NOT NULL,
  agosto_5 NUMERIC NOT NULL,
  agosto_6 NUMERIC NOT NULL,
  septiembre_1 NUMERIC NOT NULL,
  septiembre_2 NUMERIC NOT NULL,
  septiembre_3 NUMERIC NOT NULL,
  septiembre_4 NUMERIC NOT NULL,
  septiembre_5 NUMERIC NOT NULL,
  septiembre_6 NUMERIC NOT NULL,
  subtotal_1 NUMERIC NOT NULL,
  subtotal_2 NUMERIC NOT NULL,
  subtotal_3 NUMERIC NOT NULL,
  subtotal_4 NUMERIC NOT NULL,
  subtotal_5 NUMERIC NOT NULL,
  subtotal_6 NUMERIC NOT NULL,
  octubre_1 NUMERIC NOT NULL,
  octubre_2 NUMERIC NOT NULL,
  octubre_3 NUMERIC NOT NULL,
  octubre_4 NUMERIC NOT NULL,
  octubre_5 NUMERIC NOT NULL,
  octubre_6 NUMERIC NOT NULL,
  noviembre_1 NUMERIC NOT NULL,
  noviembre_2 NUMERIC NOT NULL,
  noviembre_3 NUMERIC NOT NULL,
  noviembre_4 NUMERIC NOT NULL,
  noviembre_5 NUMERIC NOT NULL,
  noviembre_6 NUMERIC NOT NULL,
  diciembre_1 NUMERIC NOT NULL,
  diciembre_2 NUMERIC NOT NULL,
  diciembre_3 NUMERIC NOT NULL,
  diciembre_4 NUMERIC NOT NULL,
  diciembre_5 NUMERIC NOT NULL,
  diciembre_6 NUMERIC NOT NULL,
  subtotal_11 NUMERIC NOT NULL,
  subtotal_12 NUMERIC NOT NULL,
  subtotal_13 NUMERIC NOT NULL,
  subtotal_14 NUMERIC NOT NULL,
  subtotal_15 NUMERIC NOT NULL,
  subtotal_16 NUMERIC NOT NULL,
  año_1 INTEGER NOT NULL,
  enero_1 NUMERIC NOT NULL,
  enero_2 NUMERIC NOT NULL,
  enero_3 NUMERIC NOT NULL,
  enero_4 NUMERIC NOT NULL,
  enero_5 NUMERIC NOT NULL,
  enero_6 NUMERIC NOT NULL,
  febrero_1 NUMERIC NOT NULL,
  febrero_2 NUMERIC NOT NULL,
  febrero_3 NUMERIC NOT NULL,
  febrero_4 NUMERIC NOT NULL,
  febrero_5 NUMERIC NOT NULL,
  febrero_6 NUMERIC NOT NULL,
  marzo_1 NUMERIC NOT NULL,
  marzo_2 NUMERIC NOT NULL,
  marzo_3 NUMERIC NOT NULL,
  marzo_4 NUMERIC NOT NULL,
  marzo_5 NUMERIC NOT NULL,
  marzo_6 NUMERIC NOT NULL,
  subtotal_21 NUMERIC NOT NULL,
  subtotal_22 NUMERIC NOT NULL,
  subtotal_23 NUMERIC NOT NULL,
  subtotal_24 NUMERIC NOT NULL,
  subtotal_25 NUMERIC NOT NULL,
  subtotal_26 NUMERIC NOT NULL,
  abril_1 NUMERIC NOT NULL,
  abril_2 NUMERIC NOT NULL,
  abril_3 NUMERIC NOT NULL,
  abril_4 NUMERIC NOT NULL,
  abril_5 NUMERIC NOT NULL,
  abril_6 NUMERIC NOT NULL,
  mayo_1 NUMERIC NOT NULL,
  mayo_2 NUMERIC NOT NULL,
  mayo_3 NUMERIC NOT NULL,
  mayo_4 NUMERIC NOT NULL,
  mayo_5 NUMERIC NOT NULL,
  mayo_6 NUMERIC NOT NULL,
  junio_1 NUMERIC NOT NULL,
  junio_2 NUMERIC NOT NULL,
  junio_3 NUMERIC NOT NULL,
  junio_4 NUMERIC NOT NULL,
  junio_5 NUMERIC NOT NULL,
  junio_6 NUMERIC NOT NULL,
  subtotal_31 NUMERIC NOT NULL,
  subtotal_32 NUMERIC NOT NULL,
  subtotal_33 NUMERIC NOT NULL,
  subtotal_34 NUMERIC NOT NULL,
  subtotal_35 NUMERIC NOT NULL,
  subtotal_36 NUMERIC NOT NULL,
  total_1 NUMERIC NOT NULL,
  total_2 NUMERIC NOT NULL,
  total_3 NUMERIC NOT NULL,
  total_4 NUMERIC NOT NULL,
  total_5 NUMERIC NOT NULL,
  total_6 NUMERIC NOT NULL,
  signature TEXT NOT NULL,
  name TEXT NOT NULL,
  title TEXT NOT NULL,
  phone TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_529 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_536_2 {
  id INTEGER,
  form_id INTEGER,
  start_year INTEGER NOT NULL,
  end_year INTEGER NOT NULL,
  inventario1 NUMERIC NOT NULL,
  inventario2 NUMERIC NOT NULL,
  compras1 NUMERIC NOT NULL,
  compras2 NUMERIC NOT NULL,
  depre1 NUMERIC NOT NULL,
  depre2 NUMERIC NOT NULL,
  maquinaria1 NUMERIC NOT NULL,
  maquinaria2 NUMERIC NOT NULL,
  equipo1 NUMERIC NOT NULL,
  equipo2 NUMERIC NOT NULL,
  computadora1 NUMERIC NOT NULL,
  computadora2 NUMERIC NOT NULL,
  alquiler1 NUMERIC NOT NULL,
  alquiler2 NUMERIC NOT NULL,
  licencia1 NUMERIC NOT NULL,
  licencia2 NUMERIC NOT NULL,
  company_name TEXT NOT NULL,
  phone TEXT NOT NULL,
  name_title TEXT NOT NULL,
  date TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_544 {
  id INTEGER,
  form_id INTEGER,
  institucion1 TEXT NOT NULL,
  proposito1 TEXT NOT NULL,
  dolares1 NUMERIC NOT NULL,
  institucion2 TEXT NOT NULL,
  proposito2 TEXT NOT NULL,
  dolares2 NUMERIC NOT NULL,
  institucion3 TEXT NOT NULL,
  proposito3 TEXT NOT NULL,
  dolares3 NUMERIC NOT NULL,
  institucion4 TEXT NOT NULL,
  proposito4 TEXT NOT NULL,
  dolares4 NUMERIC NOT NULL,
  institucion5 TEXT NOT NULL,
  proposito5 TEXT NOT NULL,
  dolares5 NUMERIC NOT NULL,
  institucion6 TEXT NOT NULL,
  proposito6 TEXT NOT NULL,
  dolares6 NUMERIC NOT NULL,
  institucion7 TEXT NOT NULL,
  proposito7 TEXT NOT NULL,
  dolares7 NUMERIC NOT NULL,
  institucion8 TEXT NOT NULL,
  proposito8 TEXT NOT NULL,
  dolares8 NUMERIC NOT NULL,
  institucion9 TEXT NOT NULL,
  proposito9 TEXT NOT NULL,
  dolares9 NUMERIC NOT NULL,
  institucion10 TEXT NOT NULL,
  proposito10 TEXT NOT NULL,
  dolares10 NUMERIC NOT NULL,
  institucion11 TEXT NOT NULL,
  proposito11 TEXT NOT NULL,
  dolares11 NUMERIC NOT NULL,
  institucion12 TEXT NOT NULL,
  proposito12 TEXT NOT NULL,
  dolares12 NUMERIC NOT NULL,
  institucion13 TEXT NOT NULL,
  proposito13 TEXT NOT NULL,
  dolares13 NUMERIC NOT NULL,
  institucion14 TEXT NOT NULL,
  proposito14 TEXT NOT NULL,
  dolares14 NUMERIC NOT NULL,
  operation_expenses NUMERIC NOT NULL,
  salary NUMERIC NOT NULL,
  SS_SD_SR_beneficios_marginales NUMERIC NOT NULL,
  servicios_profecionales_c NUMERIC NOT NULL,
  intereses NUMERIC NOT NULL,
  other_gastos NUMERIC NOT NULL,
  to_people NUMERIC NOT NULL,
  servicios_profecionales_a NUMERIC NOT NULL,
  pension NUMERIC NOT NULL,
  name_other_1 TEXT NOT NULL,
  quantity_other_1 NUMERIC NOT NULL,
  name_other_2 TEXT NOT NULL,
  quantity_other_2 NUMERIC NOT NULL,
  name_other_3 TEXT NOT NULL,
  quantity_other_3 NUMERIC NOT NULL,
  name_other_4 TEXT NOT NULL,
  quantity_other_4 NUMERIC NOT NULL,
  agencia TEXT NOT NULL,
  prep TEXT NOT NULL,
  titulo TEXT NOT NULL,
  telefono TEXT NOT NULL,
  fecha TEXT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_544_1 {
  id INTEGER,
  form_id INTEGER,
  university_name TEXT NOT NULL,
  phone TEXT NOT NULL,
  contact_person TEXT NOT NULL,
  direction TEXT NOT NULL,
  email TEXT NOT NULL,
  federal_agency_name_1 TEXT NOT NULL,
  federal_program_1 TEXT NOT NULL,
  federal_recieived_amount_1 NUMERIC NOT NULL,
  federal_date_receipt_1 TEXT NOT NULL,
  federal_agency_name_2 TEXT NOT NULL,
  federal_program_2 TEXT NOT NULL,
  federal_recieived_amount_2 NUMERIC NOT NULL,
  federal_date_receipt_2 TEXT NOT NULL,
  federal_agency_name_3 TEXT NOT NULL,
  federal_program_3 TEXT NOT NULL,
  federal_recieived_amount_3 NUMERIC NOT NULL,
  federal_date_receipt_3 TEXT NOT NULL,
  federal_agency_name_4 TEXT NOT NULL,
  federal_program_4 TEXT NOT NULL,
  federal_recieived_amount_4 NUMERIC NOT NULL,
  federal_date_receipt_4 TEXT NOT NULL,
  federal_agency_name_5 TEXT NOT NULL,
  federal_program_5 TEXT NOT NULL,
  federal_recieived_amount_5 NUMERIC NOT NULL,
  federal_date_receipt_5 TEXT NOT NULL,
  federal_agency_name_6 TEXT NOT NULL,
  federal_program_6 TEXT NOT NULL,
  federal_recieived_amount_6 NUMERIC NOT NULL,
  federal_date_receipt_6 TEXT NOT NULL,
  federal_agency_name_7 TEXT NOT NULL,
  federal_program_7 TEXT NOT NULL,
  federal_recieived_amount_7 NUMERIC NOT NULL,
  federal_date_receipt_7 TEXT NOT NULL,
  federal_agency_name_8 TEXT NOT NULL,
  federal_program_8 TEXT NOT NULL,
  federal_recieived_amount_8 NUMERIC NOT NULL,
  federal_date_receipt_8 TEXT NOT NULL,
  local_agency_name_1 TEXT NOT NULL,
  agency_program_1 TEXT NOT NULL,
  agency_recieived_amount_1 NUMERIC NOT NULL,
  agency_date_receipt_1 TEXT NOT NULL,
  local_agency_name_2 TEXT NOT NULL,
  agency_program_2 TEXT NOT NULL,
  agency_recieived_amount_2 NUMERIC NOT NULL,
  agency_date_receipt_2 TEXT NOT NULL,
  local_agency_name_3 TEXT NOT NULL,
  agency_program_3 TEXT NOT NULL,
  agency_recieived_amount_3 NUMERIC NOT NULL,
  agency_date_receipt_3 TEXT NOT NULL,
  local_agency_name_4 TEXT NOT NULL,
  agency_program_4 TEXT NOT NULL,
  agency_recieived_amount_4 NUMERIC NOT NULL,
  agency_date_receipt_4 TEXT NOT NULL,
  local_agency_name_5 TEXT NOT NULL,
  agency_program_5 TEXT NOT NULL,
  agency_recieived_amount_5 NUMERIC NOT NULL,
  agency_date_receipt_5 TEXT NOT NULL,
  total_students_enrolled INTEGER NOT NULL,
  students_recived_amount NUMERIC NOT NULL,
  total_pell_grant_students INTEGER NOT NULL,
  pell_grant_students_amount NUMERIC NOT NULL,
  total_no_resident_student INTEGER NOT NULL,
  no_resident_student_amount NUMERIC NOT NULL,
  no_resident_students_bills NUMERIC NOT NULL,
  loans_granted INTEGER NOT NULL,
  loans_granted_amount NUMERIC NOT NULL,
  donations_institution_name_1 TEXT NOT NULL,
  donations_amount_1 NUMERIC NOT NULL,
  donations_date_1 TEXT NOT NULL,
  donations_institution_name_2 TEXT NOT NULL,
  donations_amount_2 NUMERIC NOT NULL,
  donations_date_2 TEXT NOT NULL,
  donations_institution_name_3 TEXT NOT NULL,
  donations_amount_3 NUMERIC NOT NULL,
  donations_date_3 TEXT NOT NULL,
  donations_institution_name_4 TEXT NOT NULL,
  donations_amount_4 NUMERIC NOT NULL,
  donations_date_4 TEXT NOT NULL,
  donations_institution_name_5 TEXT NOT NULL,
  donations_amount_5 NUMERIC NOT NULL,
  donations_date_5 TEXT NOT NULL,
  profesional_services_amount INTEGER NOT NULL,
  profesional_services_payment NUMERIC NOT NULL,
  other_payment_relations_1 TEXT NOT NULL,
  other_payment_relations_amount_1 INTEGER NOT NULL,
  other_payment_relations_payment_1 NUMERIC NOT NULL,
  other_payment_relations_2 TEXT NOT NULL,
  other_payment_relations_amount_2 INTEGER NOT NULL,
  other_payment_relations_payment_2 NUMERIC NOT NULL,
  other_payment_relations_3 TEXT NOT NULL,
  other_payment_relations_amount_3 INTEGER NOT NULL,
  other_payment_relations_payment_3 NUMERIC NOT NULL,
  other_payment_relations_4 TEXT NOT NULL,
  other_payment_relations_amount_4 INTEGER NOT NULL,
  other_payment_relations_payment_4 NUMERIC NOT NULL,
  acquired_value NUMERIC NOT NULL,
  investment_amount NUMERIC NOT NULL,
  recived_interest NUMERIC NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_547 {
  id INTEGER,
  form_id INTEGER,
  agency_form TEXT NOT NULL,
  agency_to TEXT NOT NULL,
  salaries_wages NUMERIC NOT NULL,
  civil_service NUMERIC NOT NULL,
  federal_employee_retirement NUMERIC NOT NULL,
  thrift_savings_disbursements NUMERIC NOT NULL,
  socal_security NUMERIC NOT NULL,
  life_insurance_health_disbursements NUMERIC NOT NULL,
  other_disbursements NUMERIC NOT NULL,
  construction_contracts NUMERIC NOT NULL,
  rent_disbursements NUMERIC NOT NULL,
  other_purchases NUMERIC NOT NULL,
  equipment_supplies NUMERIC NOT NULL,
  rent_sales NUMERIC NOT NULL,
  other_sales NUMERIC NOT NULL,
  income_tax NUMERIC NOT NULL,
  other_taxes_licenses NUMERIC NOT NULL,
  fines_penalties NUMERIC NOT NULL,
  interest NUMERIC NOT NULL,
  other_collections_1 TEXT NOT NULL,
  other_collections_amount_1 NUMERIC NOT NULL,
  other_collections_2 TEXT NOT NULL,
  other_collections_amount_2 NUMERIC NOT NULL,
  other_collections_3 TEXT NOT NULL,
  other_collections_amount_3 NUMERIC NOT NULL,
  civil_service_2 NUMERIC NOT NULL,
  federal_employee NUMERIC NOT NULL,
  thrift_saving_deductions NUMERIC NOT NULL,
  social_security NUMERIC NOT NULL,
  life_insurance_health_deductions NUMERIC NOT NULL,
  income_tax_deductions NUMERIC NOT NULL,
  saving_bonds NUMERIC NOT NULL,
  other_deductions TEXT NOT NULL,
  other_deductions_amount NUMERIC NOT NULL,
  commonwealth NUMERIC NOT NULL,
  municipal NUMERIC NOT NULL,
  individuals_private_institutions NUMERIC NOT NULL,
  death_disability NUMERIC NOT NULL,
  other_payments_1 NUMERIC NOT NULL,
  other_payments_amount_1 NUMERIC NOT NULL,
  other_payments_2 NUMERIC NOT NULL,
  other_payments_amount_2 NUMERIC NOT NULL,
  loans_advances NUMERIC NOT NULL,
  repayments_loans NUMERIC NOT NULL,
  total_loans_amount NUMERIC NOT NULL,
  loans_cancelled NUMERIC NOT NULL,
  other_credits NUMERIC NOT NULL,
  loans_and_advances TEXT NOT NULL,
  loans_and_advances_amount NUMERIC NOT NULL,
  interest_collected NUMERIC NOT NULL,
  forgiveness_credit NUMERIC NOT NULL,
  reporting_agency NUMERIC NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}


--INGRESO NETO --
CREATE TABLE IP_110 (
  id INTEGER,
  form_id INTEGER,
  company_name TEXT NOT NULL,
  address TEXT NOT NULL,
  email TEXT NOT NULL,
  liaison_officer TEXT NOT NULL,
  ssn TEXT NOT NULL,
  tel TEXT NOT NULL,
  fax TEXT,
  legal_form TEXT NOT NULL,
  cfc TEXT NOT NULL,
  business_type TEXT NOT NULL,
  business_function TEXT NOT NULL,
  branches TEXT NOT NULL,
  closing_date TEXT NOT NULL,
  start_year INTEGER NOT NULL,
  end_year INTEGER NOT NULL,
  incomes_services_revenues_1 NUMERIC NOT NULL,
  incomes_services_revenues_2 NUMERIC NOT NULL,
  incomes_industries_1 NUMERIC NOT NULL,
  incomes_industries_2 NUMERIC NOT NULL,
  incomes_persons_1 NUMERIC NOT NULL,
  incomes_persons_2 NUMERIC NOT NULL,
  incomes_sale_merchandise_1 NUMERIC NOT NULL,
  incomes_sale_merchandise_2 NUMERIC NOT NULL,
  incomes_rents_1 NUMERIC NOT NULL,
  incomes_rents_2 NUMERIC NOT NULL,
  incomes_interests_1 NUMERIC NOT NULL,
  incomes_interests_2 NUMERIC NOT NULL,
  incomes_capital_gain_loss_1 NUMERIC NOT NULL,
  others_incomes_1 NUMERIC NOT NULL,
  total_income_1 NUMERIC NOT NULL,
  total_income_2 NUMERIC NOT NULL,
  expenses_1 NUMERIC NOT NULL,
  expenses_2 NUMERIC NOT NULL,
  expenses_salaries_wages_bonus_1 NUMERIC NOT NULL,
  expenses_salaries_wages_bonus_2 NUMERIC NOT NULL,
  expenses_interests_1 NUMERIC NOT NULL,
  expenses_interests_2 NUMERIC NOT NULL,
  expenses_rents_1 NUMERIC NOT NULL,
  expenses_rents_2 NUMERIC NOT NULL,
  expenses_depreciation_1 NUMERIC NOT NULL,
  expenses_depreciation_2 NUMERIC NOT NULL,
  expenses_bad_debts_1 NUMERIC NOT NULL,
  expenses_bad_debts_2 NUMERIC NOT NULL,
  expenses_donation_1 NUMERIC NOT NULL,
  expenses_donation_2 NUMERIC NOT NULL,
  expenses_sales_tax_1 NUMERIC NOT NULL,
  expenses_sales_tax_2 NUMERIC NOT NULL,
  expenses_machinery_1 NUMERIC NOT NULL,
  expenses_machinery_2 NUMERIC NOT NULL,
  other_purchases_1 NUMERIC NOT NULL,
  other_purchases_2 NUMERIC NOT NULL,
  licenses_1 NUMERIC NOT NULL,
  licenses_2 NUMERIC NOT NULL,
  other_expenses_1 NUMERIC NOT NULL,
  other_expenses_2 NUMERIC NOT NULL,
  total_expenses_1 NUMERIC NOT NULL,
  total_expenses_2 NUMERIC NOT NULL,
  net_profit_1 NUMERIC NOT NULL,
  net_profit_2 NUMERIC NOT NULL,
  net_profit_income_tax_1 NUMERIC NOT NULL,
  profit_after_tax_1 NUMERIC NOT NULL,
  profit_after_tax_2 NUMERIC NOT NULL,
  withheld_tax_1 NUMERIC NOT NULL,
  withheld_tax_2 NUMERIC NOT NULL,
  signature TEXT NOT NULL,
  rank TEXT,

  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id)
);


CREATE TABLE IP_210 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_220 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_230 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_310 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_310b {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_420 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_440 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_440g {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_480 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_480a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_490 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_510 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_520s {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_530 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540J {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540P {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540S {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540a {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_540v {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_610 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_620 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_710 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_720 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE IP_810 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63110 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63111 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_63210 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}

CREATE TABLE JP_560_2 {
  id INTEGER,
  form_id INTEGER,


  PRIMARY KEY (id),
  FOREIGN KEY (form_id) REFERENCES Forms(id),
}