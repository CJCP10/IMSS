import pandas as pd
import numpy as np
import openpyxl



# Diccionarios
meses = {"enero":"01","Febrero":"02","marzo":"03","abril":"04","mayo":"05","junio":"06","julio":"07","agosto":"08","septiembre":"09","octubre":"10","noviembre":"11","diciembre":"12"}
encuestas = {"2011":"noviembre","2012":"septiembre","2013":"julio","2014":"octubre","2015":"noviembre","2016":"noviembre","2017":"noviembre","2018":"noviembre",
            "2019":"noviembre","2022":"noviembre"}
años = ["2011","2012","2013","2014","2015","2016","2017","2018","2019","2022"]



# Lectura de archivos de las encuestas EnSat y EnCal
EnCals = []
habientes_años = []
for i in años:
    año = i
    mes = encuestas[año]
    #archivo_e = año + "_" + mes + "_nacional.csv"
    archivo_e = "Ensat_" + año + ".xlsx"
    #encuesta =pd.read_csv("C:/Users/ccamacho/OneDrive - SESNA/DIA/Proyectos Especiales/IMSS/Bases_ensat/Encuestas_EnCal/" + archivo_e , encoding="windows-1252")
    encuesta_1=pd.read_excel(archivo_e, sheet_name="Completo")
    #EnCals.append(encuesta_1) 

    # Lectura de la base de Derechohabientes

    valor = meses[mes]
    archivo_d = "Derechohabientes_" + año + "_" + valor + ".xlsx"
    derechohabientes_1=pd.read_excel("C:/Users/ccamacho/OneDrive - SESNA/DIA/Proyectos Especiales/IMSS/Derechohabientes/" + archivo_d, sheet_name="Unicos")
    #habientes_años.append(derechohabientes_1)


    # Verificamos las dimensiones de las tablas
    print("La dimensión de la encuesta es: " + str(encuesta_1.shape))
    print("La dimensión de la base Derechohabientes es: " + str(derechohabientes_1.shape))


    encuesta = encuesta_1.copy()
    derechohabientes = derechohabientes_1.copy()
    if año == "2011":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat3","Btratou","Atn1fam","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Atn1fam"] = indicadores["Atn1fam"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2012":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat2","Sat3","Btratou","Corrup","Atn1fam","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat2"] = indicadores["Sat2"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Corrup"] = indicadores["Corrup"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Atn1fam"] = indicadores["Atn1fam"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2013":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat3","Btratou","Corrup","Atn1fam","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Corrup"] = indicadores["Corrup"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Atn1fam"] = indicadores["Atn1fam"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2014" or año == "2015":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat3","Btratou","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2016" or año == "2017":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat3","Recomej_A","Recomej_B","Recomej_C","Btratou","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Recomej_A"] = indicadores["Recomej_A"].astype(str)
        indicadores["Recomej_B"] = indicadores["Recomej_B"].astype(str)
        indicadores["Recomej_C"] = indicadores["Recomej_C"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2018":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat3","Comincomcons","Btratou","Recomej_A","Recomej_B","Recomej_C","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Comincomcons"] = indicadores["Comincomcons"].astype(str)
        indicadores["Recomej_A"] = indicadores["Recomej_A"].astype(str)
        indicadores["Recomej_B"] = indicadores["Recomej_B"].astype(str)
        indicadores["Recomej_C"] = indicadores["Recomej_C"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2019":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","Sat1","Sat3","Comincom","Btratou","Totmed","Fe_Finalnr","TOT_CASOS"]]
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Comincom"] = indicadores["Comincom"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)
    elif año == "2022":
        indicadores = pd.merge(encuesta, derechohabientes, how="left", on="CLUES")[["CLUES","sat1","sat3","comincomcons","btratou","atn1fam","atnpref","atnpref2_a","totmed","FE_FinalNR","TOT_CASOS"]] 
        indicadores = indicadores.rename(columns={"sat1":"Sat1","sat3":"Sat3","comincomcons":"Comincomcons",
                                                "btratou":"Btratou","atn1fam":"Atn1fam","atnpref":"Atnpref",
                                                "atnpref2_a":"Atnpref2_a","totmed":"Totmed","FE_FinalNR":"Fe_Finalnr"})
        # Cambamos el tipo de dato de cada una de las columnas
        indicadores["Sat1"] = indicadores["Sat1"].astype(str)
        indicadores["Sat3"] = indicadores["Sat3"].astype(str)
        indicadores["Comincomcons"] = indicadores["Comincomcons"].astype(str)
        indicadores["Btratou"] = indicadores["Btratou"].astype(str)
        indicadores["Atn1fam"] = indicadores["Atn1fam"].astype(str)
        indicadores["Atnpref"] = indicadores["Atnpref"].astype(str)
        indicadores["Atnpref2_a"] = indicadores["Atnpref2_a"].astype(str)
        indicadores["Totmed"] = indicadores["Totmed"].astype(str)
        indicadores["Fe_Finalnr"] = indicadores["Fe_Finalnr"].astype(float)



    print("La dimensión de la encuesta es: " + str(indicadores.shape))  # Dimensión de la tabla 
    print(indicadores.isna().sum())  # Sólo una vista de cuantos datos faltante tenemos.
    indicadores.head()




    #########################################################################################################
    ################################################# Sat1 ##################################################
    #########################################################################################################    
    sat1 = indicadores.groupby(["CLUES", "Sat1","Fe_Finalnr"]).agg(conteo = ("Sat1", "count")).reset_index() #Agrupamos por CLUES y contamos las respuestas
    sat1 = sat1.query('Sat1 == "4" or Sat1 == "5"')   # Contamos a todas las personas que respondieron 4 o 5, y agrupamos por unidad médica
    sat1['Fe_Finalnr'] = sat1['Fe_Finalnr'] * sat1['conteo']
    sat1 = sat1.groupby("CLUES").sum().reset_index()

                                    ## PENDIENTE ##
    # if año == "2012":
    #     sat2 = indicadores.groupby(["CLUES","Sat2","Fe_Finalnr"]).agg(conteo = ("Sat2","count")).reset_index()
    #     sat2 = sat2.query('Sat2 == "4" or Sat2 == "5"') # Contamos a todas las personas que respondieron 4 o 5, y agrupamos por unidad médica
    #     sat2['Fe_Finalnr'] = sat2['Fe_Finalnr'] * sat2['conteo']
    #     sat2 = sat2.groupby("CLUES").sum().reset_index()
    #     sat2["Comentarios"] = "Variable Sat2" 
    #     sat1 = pd.concat([sat1,sat2],axis=0)

    ###################################################################################################################
    ################################################# Sat1_indicador ##################################################
    ################################################################################################################### 
    sat1_i = sat1.copy()   # Hacemos una copia
    sat1_i = pd.merge(sat1_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
    sat1_i['Medida'] = ((sat1_i['Fe_Finalnr_x'] * sat1_i['conteo'])/sat1_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
    sat1_i = sat1_i.drop_duplicates()    # Eliminamos duplicados
    sat1_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
    sat1_i["Año"] = año
    sat1_i["Indicador"] = "Número de personas insatisfechas con la atención MÉDICA por cada 1,000 derechohabientes, por unidad de atención médica."
    del sat1_i['TOT_CASOS']
    del sat1_i['conteo']
    del sat1_i['Fe_Finalnr_x']

    print("Se calculo el indicador 1")


    #########################################################################################################
    ################################################# Sat3 ##################################################
    #########################################################################################################    
    sat3 = indicadores.groupby(["CLUES", "Sat3","Fe_Finalnr"]).agg(conteo = ("Sat3", "count")).reset_index()
    sat3 = sat3.query('Sat3 == "4" or Sat3 == "5"') # Contamos a todas las personas que respondieron 4 o 5, y agrupamos por unidad médica
    sat3['Fe_Finalnr'] = sat3['Fe_Finalnr'] * sat3['conteo']
    sat3 = sat3.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# Sat3_indicador ##################################################
    ################################################################################################################### 
    sat3_i = sat3.copy()   # Hacemos una copia
    sat3_i = pd.merge(sat3_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
    sat3_i['Medida'] = ((sat3_i['Fe_Finalnr_x'] * sat3_i['conteo'])/sat3_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
    sat3_i = sat3_i.drop_duplicates()    # Eliminamos duplicados
    sat3_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
    sat3_i["Año"] = año
    sat3_i["Indicador"] = "Número de personas insatisfechas con la atención GENERAL por cada 1,000 derechohabientes, por unidad de atención médica."
    del sat3_i['TOT_CASOS']
    del sat3_i['conteo']
    del sat3_i['Fe_Finalnr_x']

    print("Se calculo el indicador 2")


    #########################################################################################################
    ################################################# Comincomcons ##########################################
    #########################################################################################################    
    if año == "2018" or  año == "2022":
        comincomcons = indicadores.groupby(["CLUES", "Comincomcons","Fe_Finalnr"]).agg(conteo = ("Comincomcons", "count")).reset_index()
        comincomcons = comincomcons.query('Comincomcons == "1" or Comincomcons == "1.0"') # Contamos a todas las personas que respondieron 1, y agrupamos por unidad médica
        comincomcons['Fe_Finalnr'] = comincomcons['Fe_Finalnr'] * comincomcons['conteo']
        comincomcons = comincomcons.groupby("CLUES").sum().reset_index()
    ###################################################################################################################
    ################################################# Comincomcons_indicador ##################################################
    ################################################################################################################### 
        comincomcons_i = comincomcons.copy()   # Hacemos una copia
        comincomcons_i = pd.merge(comincomcons_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        comincomcons_i['Medida'] = ((comincomcons_i['Fe_Finalnr_x'] * comincomcons_i['conteo'])/comincomcons_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        comincomcons_i = comincomcons_i.drop_duplicates()    # Eliminamos duplicados
        comincomcons_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        comincomcons_i["Año"] = año
        comincomcons_i["Indicador"] = "Número de personas que se sintieron incómodas, discriminadas o humilladas por parte del personal de salud por 1,000 derechohabientes, por unidad de atención médica."
        del comincomcons_i['TOT_CASOS']
        del comincomcons_i['conteo']
        del comincomcons_i['Fe_Finalnr_x']

        print("Se calculo el indicador 3")

    elif año == "2019":
        comincomcons = indicadores.groupby(["CLUES", "Comincom","Fe_Finalnr"]).agg(conteo = ("Comincom", "count")).reset_index()
        comincomcons = comincomcons.query('Comincom == "1" or Comincom == "1.0"') # Contamos a todas las personas que respondieron 1, y agrupamos por unidad médica
        comincomcons['Fe_Finalnr'] = comincomcons['Fe_Finalnr'] * comincomcons['conteo']
        comincomcons = comincomcons.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# Comincomcons_indicador ##################################################
    ################################################################################################################### 
        comincomcons_i = comincomcons.copy()   # Hacemos una copia
        comincomcons_i = pd.merge(comincomcons_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        comincomcons_i['Medida'] = ((comincomcons_i['Fe_Finalnr_x'] * comincomcons_i['conteo'])/comincomcons_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        comincomcons_i = comincomcons_i.drop_duplicates()    # Eliminamos duplicados
        comincomcons_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        comincomcons_i["Año"] = año
        comincomcons_i["Indicador"] = "Número de personas que se sintieron incómodas, discriminadas o humilladas por parte del personal de salud por 1,000 derechohabientes, por unidad de atención médica."
        del comincomcons_i['TOT_CASOS']
        del comincomcons_i['conteo']
        del comincomcons_i['Fe_Finalnr_x']

        print("Se calculo el indicador 3")


    #########################################################################################################
    ################################################# Recomej ##################################################
    #########################################################################################################    
    if año == "2016" or año == "2017":
        Recomej_A = indicadores.groupby(["CLUES", "Recomej_A","Fe_Finalnr"]).agg(conteo = ("Recomej_A", "count")).reset_index()
        Recomej_A = Recomej_A.query('Recomej_A == "118"') # Contamos a todas las personas que respondieron 118, y agrupamos por unidad médica
        Recomej_A['Fe_Finalnr'] = Recomej_A['Fe_Finalnr'] * Recomej_A['conteo']
        Recomej_A = Recomej_A.groupby("CLUES").sum().reset_index()
        Recomej_A['Recomej'] = "Recomej_A"

        Recomej_B = indicadores.groupby(["CLUES", "Recomej_B","Fe_Finalnr"]).agg(conteo = ("Recomej_B", "count")).reset_index()
        Recomej_B = Recomej_B.query('Recomej_B == "118.0"') # Contamos a todas las personas que respondieron 118, y agrupamos por unidad médica
        Recomej_B['Fe_Finalnr'] = Recomej_B['Fe_Finalnr'] * Recomej_B['conteo']
        Recomej_B = Recomej_B.groupby("CLUES").sum().reset_index()
        Recomej_B['Recomej'] = "Recomej_B"

        Recomej_C = indicadores.groupby(["CLUES", "Recomej_C","Fe_Finalnr"]).agg(conteo = ("Recomej_C", "count")).reset_index()
        Recomej_C = Recomej_C.query('Recomej_C == "118.0"') # Contamos a todas las personas que respondieron 118, y agrupamos por unidad médica
        Recomej_C['Fe_Finalnr'] = Recomej_C['Fe_Finalnr'] * Recomej_C['conteo']
        Recomej_C = Recomej_C.groupby("CLUES").sum().reset_index()
        Recomej_C['Recomej'] = "Recomej_C"

        recomej = pd.concat([Recomej_A, Recomej_B, Recomej_C], axis=0)

        recomej_i = recomej.copy()   # Hacemos una copia
        recomej_i = pd.merge(recomej_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","Recomej","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        recomej_i['Medida'] = ((recomej_i['Fe_Finalnr_x'] * recomej_i['conteo'])/recomej_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        recomej_i = recomej_i.drop_duplicates()    # Eliminamos duplicados
        recomej_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        recomej_i["Año"] = año
        recomej_i["Indicador"] = "De acuerdo a su experiencia, ¿qué recomendaría para mejorar el servicio de esta unidad médica?"
        del recomej_i['TOT_CASOS']
        del recomej_i['conteo']
        del recomej_i['Fe_Finalnr_x']

    elif año == "2018":
        Recomej_A = indicadores.groupby(["CLUES", "Recomej_A","Fe_Finalnr"]).agg(conteo = ("Recomej_A", "count")).reset_index()
        Recomej_A = Recomej_A.query('Recomej_A == "55" or Recomej_A == "55.0"') # Contamos a todas las personas que respondieron 118, y agrupamos por unidad médica
        Recomej_A['Fe_Finalnr'] = Recomej_A['Fe_Finalnr'] * Recomej_A['conteo']
        Recomej_A = Recomej_A.groupby("CLUES").sum().reset_index()
        Recomej_A['Recomej'] = "Recomej_A"

        Recomej_B = indicadores.groupby(["CLUES", "Recomej_B","Fe_Finalnr"]).agg(conteo = ("Recomej_B", "count")).reset_index()
        Recomej_B = Recomej_B.query('Recomej_B == "55" or Recomej_B == "55.0"') # Contamos a todas las personas que respondieron 118, y agrupamos por unidad médica
        Recomej_B['Fe_Finalnr'] = Recomej_B['Fe_Finalnr'] * Recomej_B['conteo']
        Recomej_B = Recomej_B.groupby("CLUES").sum().reset_index()
        Recomej_B['Recomej'] = "Recomej_B"

        Recomej_C = indicadores.groupby(["CLUES", "Recomej_C","Fe_Finalnr"]).agg(conteo = ("Recomej_C", "count")).reset_index()
        Recomej_C = Recomej_C.query('Recomej_C == "55" or Recomej_C == "55.0"') # Contamos a todas las personas que respondieron 118, y agrupamos por unidad médica
        Recomej_C['Fe_Finalnr'] = Recomej_C['Fe_Finalnr'] * Recomej_C['conteo']
        Recomej_C = Recomej_C.groupby("CLUES").sum().reset_index()
        Recomej_C['Recomej'] = "Recomej_C"

        recomej = pd.concat([Recomej_A, Recomej_B, Recomej_C], axis=0)

        recomej_i = recomej.copy()   # Hacemos una copia
        recomej_i = pd.merge(recomej_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","Recomej","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        recomej_i['Medida'] = ((recomej_i['Fe_Finalnr_x'] * recomej_i['conteo'])/recomej_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        recomej_i = recomej_i.drop_duplicates()    # Eliminamos duplicados
        recomej_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        recomej_i["Año"] = año
        recomej_i["Indicador"] = "De acuerdo a su experiencia, ¿qué recomendaría para mejorar el servicio de esta unidad médica?"
        del recomej_i['TOT_CASOS']
        del recomej_i['conteo']
        del recomej_i['Fe_Finalnr_x']

    #########################################################################################################
    ################################################# Corrup ##################################################
    #########################################################################################################    
    if año == "2012" or año == "2013":
        corrup = indicadores.groupby(["CLUES", "Corrup","Fe_Finalnr"]).agg(conteo = ("Corrup", "count")).reset_index()
        corrup = corrup.query('Corrup == "1"') # Contamos a todas las personas que respondieron 1, y agrupamos por unidad médica
        corrup['Fe_Finalnr'] = corrup['Fe_Finalnr'] * corrup['conteo']
        corrup = corrup.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# Corrup_indicador ##################################################
    ################################################################################################################### 
        corrup_i = corrup.copy()   # Hacemos una copia
        corrup_i = pd.merge(corrup_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        corrup_i['Medida'] = ((corrup_i['Fe_Finalnr_x'] * corrup_i['conteo'])/corrup_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        corrup_i = corrup_i.drop_duplicates()    # Eliminamos duplicados
        corrup_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        corrup_i["Año"] = año
        corrup_i["Indicador"] = "Durante la atención que recibió en la unidad médica ¿alguien le pidió dinero o le cobró de alguna forma por brindarle el servicio?"
        del corrup_i['TOT_CASOS']
        del corrup_i['conteo']
        del corrup_i['Fe_Finalnr_x']

        print("Se calculo el indicador 4")



    #########################################################################################################
    ################################################# Btratou ##################################################
    #########################################################################################################
    if año == "2011" or año == "2012":    
        btratou = indicadores.groupby(["CLUES", "Btratou","Fe_Finalnr"]).agg(conteo = ("Btratou", "count")).reset_index()
        btratou = btratou.query('Btratou == "2"') # Contamos a todas las personas que respondieron 2, y agrupamos por unidad médica
        btratou['Fe_Finalnr'] = btratou['Fe_Finalnr'] * btratou['conteo']
        btratou = btratou.groupby("CLUES").sum().reset_index()
    else:    
        btratou = indicadores.groupby(["CLUES", "Btratou","Fe_Finalnr"]).agg(conteo = ("Btratou", "count")).reset_index()
        btratou = btratou.query('Btratou == "3" or Btratou == "4" or Btratou == "5"')  # Contamos a todas las personas que respondieron 3,4,5 y agrupamos por unidad médica
        btratou['Fe_Finalnr'] = btratou['Fe_Finalnr'] * btratou['conteo']
        btratou = btratou.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# btratou_indicador ##################################################
    ################################################################################################################### 
    btratou_i = btratou.copy()   # Hacemos una copia
    btratou_i = pd.merge(btratou_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
    btratou_i['Medida'] = ((btratou_i['Fe_Finalnr_x'] * btratou_i['conteo'])/btratou_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
    btratou_i = btratou_i.drop_duplicates()    # Eliminamos duplicados
    btratou_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
    btratou_i["Año"] = año
    btratou_i["Indicador"] = "Número de personas que calificaron regular, malo o pésimo el trato, por 1,000 derechohabientes, por unidad de atención médica."
    del btratou_i['TOT_CASOS']
    del btratou_i['conteo']
    del btratou_i['Fe_Finalnr_x']
    print("Se calculo el indicador 5")


    #########################################################################################################
    ################################################# Atn1fam ##################################################
    #########################################################################################################    
    if año == "2011" or año == "2012" or año == "2013" or año == "2022": 
        atn1fam = indicadores.groupby(["CLUES", "Atn1fam","Fe_Finalnr"]).agg(conteo = ("Atn1fam", "count")).reset_index()
        atn1fam = atn1fam.query('Atn1fam == "1"') # Contamos a todas las personas que respondieron 1, y agrupamos por unidad médica
        atn1fam['Fe_Finalnr'] = atn1fam['Fe_Finalnr'] * atn1fam['conteo']
        atn1fam = atn1fam.groupby("CLUES").sum().reset_index()
    ###################################################################################################################
    ################################################# atn1fam_indicador ##################################################
    ################################################################################################################### 
        atn1fam_i = atn1fam.copy()   # Hacemos una copia
        atn1fam_i = pd.merge(atn1fam_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        atn1fam_i['Medida'] = ((atn1fam_i['Fe_Finalnr_x'] * atn1fam_i['conteo'])/atn1fam_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        atn1fam_i = atn1fam_i.drop_duplicates()    # Eliminamos duplicados
        atn1fam_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        atn1fam_i["Año"] = año
        atn1fam_i["Indicador"] = "Número de personas que perciben que el personal de la unidad atiende primero a sus familiares/amigos, por 1,000 derechohabientes, por unidad de atención médica."
        del atn1fam_i['TOT_CASOS']
        del atn1fam_i['conteo']
        del atn1fam_i['Fe_Finalnr_x']
        print("Se calculo el indicador 6")

    #########################################################################################################
    ################################################# Atnpref ###############################################
    #########################################################################################################    
    if año == "2022":   
        atnpref = indicadores.groupby(["CLUES", "Atnpref","Fe_Finalnr"]).agg(conteo = ("Atnpref", "count")).reset_index()
        atnpref = atnpref.query('Atnpref == "1"') # Contamos a todas las personas que respondieron 1, y agrupamos por unidad médica
        atnpref['Fe_Finalnr'] = atnpref['Fe_Finalnr'] * atnpref['conteo']
        atnpref = atnpref.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# Atnpref_indicador ##################################################
    ################################################################################################################### 
        atnpref_i = atnpref.copy()   # Hacemos una copia
        atnpref_i = pd.merge(atnpref_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        atnpref_i['Medida'] = ((atnpref_i['Fe_Finalnr_x'] * atnpref_i['conteo'])/atnpref_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        atnpref_i = atnpref_i.drop_duplicates()    # Eliminamos duplicados
        atnpref_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        atnpref_i["Año"] = año
        atnpref_i["Indicador"] = "¿Considera que en esta unidad médica se brinda atención igual a todas las personas usuarias?"
        del atnpref_i['TOT_CASOS']
        del atnpref_i['conteo']
        del atnpref_i['Fe_Finalnr_x']
        print("Se calculo el indicador 7")



    #########################################################################################################
    ################################################# Atnpref2_a ############################################
    #########################################################################################################    
    if año == "2022":    
        atnpref2_1 = indicadores.groupby(["CLUES", "Atnpref2_a","Fe_Finalnr"]).agg(conteo = ("Atnpref2_a", "count")).reset_index()
        atnpref2_1 = atnpref2_1.query('Atnpref2_a == "1"') # Contamos a todas las personas que respondieron 1, y agrupamos por unidad médica
        atnpref2_1['Fe_Finalnr'] = atnpref2_1['Fe_Finalnr'] * atnpref2_1['conteo']
        atnpref2_1 = atnpref2_1.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# Atnpref2_a_indicador ##################################################
    ################################################################################################################### 
        atnpref2_a_i = atnpref2_1.copy()   # Hacemos una copia
        atnpref2_a_i = pd.merge(atnpref2_a_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
        atnpref2_a_i['Medida'] = ((atnpref2_a_i['Fe_Finalnr_x'] * atnpref2_a_i['conteo'])/atnpref2_a_i['TOT_CASOS']) *1000   # Hacemos el cálculo del indicador
        atnpref2_a_i = atnpref2_a_i.drop_duplicates()    # Eliminamos duplicados
        atnpref2_a_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
        atnpref2_a_i["Año"] = año
        atnpref2_a_i["Indicador"] = "¿Con qué frecuencia ha observado que en esta unidad médica se presentan actos que podrían percibirse como prácticas de corrupción?"
        del atnpref2_a_i['TOT_CASOS']
        del atnpref2_a_i['conteo']
        del atnpref2_a_i['Fe_Finalnr_x']
        print("Se calculo el indicador 8")


    #########################################################################################################
    ################################################# Totmed ##################################################
    #########################################################################################################    
    totmed = indicadores.groupby(["CLUES", "Totmed","Fe_Finalnr"]).agg(conteo = ("Totmed", "count")).reset_index()
    totmed = totmed.query('Totmed == "3.0" or Totmed == "3" or Totmed == 3') # Contamos a todas las personas que respondieron 3.0, y agrupamos por unidad médica
    totmed['Fe_Finalnr'] = totmed['Fe_Finalnr'] * totmed['conteo']
    totmed = totmed.groupby("CLUES").sum().reset_index()

    ###################################################################################################################
    ################################################# totmed_indicador ##################################################
    ################################################################################################################### 
    totmed_i = totmed.copy()   # Hacemos una copia
    totmed_i = pd.merge(totmed_i, indicadores, how="inner", on="CLUES")[["CLUES","Fe_Finalnr_x","conteo","TOT_CASOS"]] # Unimos el nuevo sat1_i más la tabla indicadores, y traemos ciertas columnas
    totmed_i['Medida'] = ((totmed_i['Fe_Finalnr_x'] * totmed_i['conteo'])/totmed_i['TOT_CASOS'])*1000   # Hacemos el cálculo del indicador
    totmed_i = totmed_i.drop_duplicates()    # Eliminamos duplicados
    totmed_i.dropna(subset="Medida", inplace=True)   # Eliminamos los "NA" y remplazamos el DataFrame
    totmed_i["Año"] = año
    totmed_i["Indicador"] = "Número de personas que no recibieron medicamento en la farmacia de la unidad por cada 1,000 derechohabientes, por unidad de atención médica."
    del totmed_i['TOT_CASOS']
    del totmed_i['conteo']
    del totmed_i['Fe_Finalnr_x']
    print("Se calculo el indicador 9")


    if año == "2011":
        indi_2011 = pd.concat([sat1_i,sat3_i,atn1fam_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2011")
    elif año == "2012":
        indi_2012 = pd.concat([sat1_i,sat3_i,atn1fam_i,corrup_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2012")
    elif año == "2013":
        indi_2013 = pd.concat([sat1_i,sat3_i,atn1fam_i,corrup_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2013")
    elif año == "2014":
        indi_2014 = pd.concat([sat1_i,sat3_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2014")
    elif año == "2015":
        indi_2015 = pd.concat([sat1_i,sat3_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2015")
    elif año == "2016":
        indi_2016 = pd.concat([sat1_i,sat3_i,recomej_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2016")
    elif año == "2017":
        indi_2017 = pd.concat([sat1_i,sat3_i,recomej_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2017")
    elif año == "2018":
        indi_2018 = pd.concat([sat1_i,sat3_i,comincomcons_i,recomej_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2018")
    elif año == "2019":
        indi_2019 = pd.concat([sat1_i,sat3_i,comincomcons_i,recomej_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2019")
    elif año == "2022":
        indi_2022 = pd.concat([sat1_i,sat3_i,comincomcons_i,recomej_i,atn1fam_i,atnpref_i,atnpref2_a_i,btratou_i,totmed_i],axis=0)
        print("Se creo la tabla: indi_2022")



indicadores_todo = pd.concat([indi_2011,indi_2012,indi_2013,indi_2014,indi_2015,indi_2016,indi_2017,indi_2018,indi_2019,indi_2022], axis=0)
print("Los indicadores están listos")

promedios = indicadores_todo.groupby(["Año","Indicador"]).agg(Suma_Medida=("Medida", "sum"), Conteo=("Año","count")).reset_index()
promedios["Promedio"] = promedios["Suma_Medida"] / promedios["Conteo"]
del promedios["Suma_Medida"]
del promedios["Conteo"]
print("Los promedios por año están listos")


with pd.ExcelWriter("Indicadores_todos_los_años_2.xlsx") as writer:
    indicadores_todo.to_excel(writer, sheet_name="indicadores_todo",index=False)
    promedios.to_excel(writer, sheet_name="Promedios", index=0)

print("Se creó tu archivo Excel")