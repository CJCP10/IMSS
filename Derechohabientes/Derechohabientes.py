import pandas as pd
import numpy as np
# Esta biblioteca sirve para poder eliminar los acentos
from unidecode import unidecode

claves = {"2011": "-11-30", "2012":"-09-30", "2013":"-07-31","2014":"-10-31","2015":"-11-30","2016":"-11-30","2017":"-11-30","2018":"-11-30","2019":"-11-30","2022":"-11-30"}
años = ["2011","2012","2013","2014","2015","2016","2017","2018","2019","2022"]


# Leemos el archivo de Derechohabientes que queremos
for i in años:
    codificacion = 'windows-1252'   #'utf-8'
    archivo = "pda-" + i + claves[i] +".csv"
    Derechohabientes = pd.read_csv("C:/Users/ccamacho/OneDrive - SESNA/DIA/Proyectos Especiales/IMSS/Derechohabientes/Bases_pda/"+archivo, encoding = codificacion)


    # Creamos una copia de la tabla que estaba en nuestro archivo
    DH = Derechohabientes.copy()
    print("Se hizo una copia del archivo pda: " + archivo)
    #DH.head()

    # ocuparemos esta variable mas adelante
    encabezados = DH.columns.tolist() # extraemos el nombre de la coolumna y lo transformamos a una lista para trabajar con ellos
    encabezados = ''.join(encabezados) #Este comando lo utilizamos para transformar la lista de encabezados en una cadena
    names = pd.DataFrame({"name" : [encabezados]}) # Hacemos un DataFrame con los encabezados
    names = names['name'].str.split(pat='|',expand=True) # Separamos los encabezados ya que estaban todos en una misma columna
    names = names.iloc[0] # guardamos los encabezados en la misma variable "names" ya separados

    # Dividimos toda nuestra base por el separados
    if i=="2011" or i=="2012" or i=="2013" or i=="2014" or i == "2015" or i == "2016":
        DH = DH['ID_DELEG_RP|ID_SUBDEL_RP|ID_UMF_RP|NOMBRE_UMF_RP|ST_TIT_FAM|ID_CALIDAD|CVE_GENERO|CVE_RANGO_EDAD|ST_CONSULTORIO|ID_TURNO|ID_CONSULTORIO|TOT_CASOS'].str.split(pat='|',expand=True)
    else:
        DH = DH['ID_DELEG_RP|ID_SUBDEL_RP|ID_UMF_RP|NOMBRE_UMF_RP|ST_TIT_FAM|ID_CALIDAD|CVE_SEXO|CVE_RANGO_EDAD|ST_CONSULTORIO|ID_TURNO|ID_CONSULTORIO|TOT_CASOS'].str.split(pat='|',expand=True)


    # ahgregamos los encabezados con la variable antes creada 
    #DH.columns = names
    # observamos los primeros 5 registros para verificar que los encabezados sean correctos
    #DH.head()

    # Observamos la dimensión del DF
    print("La dimensión del la pda es: " + str(DH.shape))

    #Eliminar ST_CONSULTORIO, ID_TURNO, ID_CONSULTORIO
    DH.columns = names
    DH = DH.drop(["ST_CONSULTORIO", "ID_TURNO", "ID_CONSULTORIO"], axis=1)
    #DH.head()


    # Transformamos la columna de TOT_CASOS a enteros
    DH['TOT_CASOS'] = DH['TOT_CASOS'].astype(int)
    # Agrupamos para consguir el número total de derechohabientes y reducir las filas.
    if i=="2011" or i=="2012" or i=="2013" or i=="2014" or i == "2015" or i == "2016":
        DH = DH.groupby(["ID_DELEG_RP","ID_SUBDEL_RP","ID_UMF_RP","NOMBRE_UMF_RP","ST_TIT_FAM","ID_CALIDAD","CVE_GENERO","CVE_RANGO_EDAD"]).sum().reset_index()
        DH.shape
    else:
        DH = DH.groupby(["ID_DELEG_RP","ID_SUBDEL_RP","ID_UMF_RP","NOMBRE_UMF_RP","ST_TIT_FAM","ID_CALIDAD","CVE_SEXO","CVE_RANGO_EDAD"]).sum().reset_index()
        DH.shape

    print("La totalidad de los derechohabientes es: " + str(DH['TOT_CASOS'].sum())) #Verificamos que la cifra total de derechohabientes sea congruente.+


    # Creamos una columna llamada "CLAVE" para identificar la institución
    DH['Clave_dh'] = DH["ID_DELEG_RP"] + "ID_DEL" + DH["ID_SUBDEL_RP"] + "ID_SUBDEL" + DH["ID_UMF_RP"] + "ID_UMF"
    #Vamos a mover la columna que acabamos de crear a una posición más adecuada
    clave = DH.pop('Clave_dh')
    DH.insert(3,'Clave_dh',clave) 
    DH.head()


    #Con este linea podemos saber la cantidad que hay para la columna "CLAVE"
    len(DH['Clave_dh'].unique())


    # Ahora vamos a leer el archivo, donde esta el catálogo de cada una de las instituciones
    catalogo = pd.read_excel("catalogo_UMF.xlsx", sheet_name="Catálogo")

    print(" Se leyó el catálogo de UMF, para extraer el nombre de cada una de las unidades medicas")

    # Creamos una copia con la variables siguiente
    cat = catalogo.copy()
    #cat.head(2)

    # transformamos el tipo de dato de cada columnas para poder trabajarlo
    cat["ID_SUBDEL_RP"] = cat["ID_SUBDEL_RP"].astype("Int64")
    cat["ID_UMF_RP"] = cat["ID_UMF_RP"].astype("Int64")

    # Ahora transformamos todo, a un tipo de dato str
    cat["ID_DELEG_RP"] = cat["ID_DELEG_RP"].astype(str)
    cat["ID_SUBDEL_RP"] = cat["ID_SUBDEL_RP"].astype(str)
    cat["ID_UMF_RP"] = cat["ID_UMF_RP"].astype(str)

    #Mostramos los primero cinco registros del DF
    #cat.head()


    # Creamos la clave con la que vamos a conectar la base de derechohabientes DH
    cat["Clave_Cta"] = cat["ID_DELEG_RP"] + "ID_DEL" + cat["ID_SUBDEL_RP"] + "ID_SUBDEL" + cat["ID_UMF_RP"] +"ID_UMF"
    #Vamos a mover la columna que acabamos de crear a una posición más adecuada
    clave_cta = cat.pop('Clave_Cta')
    cat.insert(3,'Clave_Cta',clave_cta) 
    #cat.head()

    # Unimos las bases DH que es la base derechohabientes, con la base catálogos
    DH_1 = pd.merge(DH, cat , left_on='Clave_dh',right_on='Clave_Cta', how='left')
    #DH_1.head()

    print("Se agregaron los nombres de las unidades exitosamente!")

    # Observamos la dimensión de nuestrp DF
    print("La dimensión de la tabla con nombres de unidades es la siguientes " + str(DH_1.shape))

    # las nombres de las columnas nos ayudan a saber cuales vamos a borrar
    #DH_1.columns

    # Eliminamos las columnas que no necesitamos
    #del DH_1['DELEGACIÓN']
    del DH_1['ID_DELEG_RP_y']
    del DH_1['ID_SUBDEL_RP_y']
    del DH_1['ID_UMF_RP_y']
    del DH_1['Clave_Cta']
    del DH_1['SUBDELEGACIÓN']

    #len(DH_1['UNIDAD'].unique())
    print("Corroboramos que la cantidad de derechohabientes sea la misma que al principio " + str(DH_1['TOT_CASOS'].sum()))

    # Creamos un nuevo DataFrame, para agrpuar y asi solo tener las unidades Unicas, un archivo más pequeño
    if i=="2011" or i=="2012" or i=="2013" or i=="2014" or i == "2015" or i == "2016":
        grupo = DH_1.copy()
        grupo["Clave"] = grupo["ID_DELEG_RP_x"] + grupo["ID_SUBDEL_RP_x"] + grupo["ID_UMF_RP_x"]
        del grupo["ID_DELEG_RP_x"], grupo["ID_SUBDEL_RP_x"], grupo["ID_UMF_RP_x"],grupo["ST_TIT_FAM"],grupo["ID_CALIDAD"]
        del grupo["CVE_GENERO"], grupo["CVE_RANGO_EDAD"]
    else:
        grupo = DH_1.copy()
        grupo["Clave"] = grupo["ID_DELEG_RP_x"] + grupo["ID_SUBDEL_RP_x"] + grupo["ID_UMF_RP_x"]
        del grupo["ID_DELEG_RP_x"], grupo["ID_SUBDEL_RP_x"], grupo["ID_UMF_RP_x"],grupo["ST_TIT_FAM"],grupo["ID_CALIDAD"]
        del grupo["CVE_SEXO"], grupo["CVE_RANGO_EDAD"]

    # Con esta línea podemos ver todas las columnas y fila donde tenemos NaN, o datos faltantes
    #grupo[grupo.isna().any(axis=1)]

    # Rellenamos todos los espacion sin dato o mejor dicho que no empataron con "Sin información"
    grupo = grupo.fillna('Sin informacion')

    # Agrupamos para poder tener por unidad medica los Derechohabientes
    #grupo = grupo.groupby(["Clave_dh","Clave","NOMBRE_UMF_RP","UNIDAD","DELEGACIÓN","ID_ENT","ENTIDAD","ID_MUN","MUNICIPIO",
    #                      "ID_LOCAL","LOCALIDAD"]).sum().reset_index()
    grupo = grupo.groupby(["Clave_dh","Clave","UNIDAD","DELEGACIÓN","ID_ENT","ENTIDAD","ID_MUN","MUNICIPIO",
                        "ID_LOCAL","LOCALIDAD"]).sum().reset_index()

    # Observamos las dimensiones de nuestro DF
    print("Agrupamos para hacer la base más manejable y la dimensión queda como: " + str(grupo.shape) + " Y el total de casos es: " + str(grupo['TOT_CASOS'].sum()))

    #Corroboramos que sigan siendo la misma cantidad de Derechohabientes
    #grupo['TOT_CASOS'].sum()

    #catalogo_D = pd.read_excel("Derechohabientes.xlsx",usecols="A,E,N") # Leemos el catálogo
    catalogo_D = pd.read_excel("catálogo_derechohabientes.xlsx",usecols="A,C,k") # Leemos el catálogo
    #catalogo_D = catalogo_D[catalogo_D["Año"] == int(i)] # Filtramos por el año que estamos trabajando
    print("Leemos el catalogo de derechohabientes para poder agregar la llave especial 'CLUE' a todas las unidades medicas")

    # Unimos el DF de grupo con el de estableciemintos para poder encontrarle el CLUE a cada unidad medica
    catalogo_b = catalogo_D.copy()
    clues = pd.merge(grupo, catalogo_b, left_on='Clave_dh',right_on='Clave_dh', how='left') 
    del clues["UNIDAD_y"]
    #clues.head(2)

    # Observamos la dimensión de nuestro nuevo DF
    print("Verificamos la dimensión de la tabla ahora con sus clue correspondientes" + str(clues.shape))

    # Observamos la cantidad de datos unicos que tenemos en CLUE
    # lo que siginfica que es el número que coicideron
    print("Tenemos la cantidad de clues unicas que es: " + str(len(clues['CLUES'].unique())))

    # Esta nueva base se ocupara para poder traer las variables que nos hacen falta como los "CLUES", "Lat", "Lon"
    establecimientos = pd.read_excel('C:/Users/ccamacho/OneDrive - SESNA/DIA/Proyectos Especiales/IMSS/Bases_Quejas/ESTABLECIMIENTO_SALUD_202308.xlsx', usecols="A,E,H,I,L,M,AQ,AT,BA,BB")

    # Creamos una copia
    Esta = establecimientos.copy()
    print("Creamos una copia de la base de establecimientos para obtener información de las unidades médicas, como la latitud y longitud")
    #Esta.head(2)

    clues = pd.merge(clues, Esta, left_on='CLUES',right_on='CLUES', how='left') 
    clues = clues.rename(columns={"UNIDAD_x":"UNIDAD"})
    #clues.head(2)

    #clues.columns


    # Eliminamos duplicados
    #clues = clues.drop_duplicates(subset=['Clave_dh','Clave','NOMBRE_UMF_RP','UNIDAD','DELEGACIÓN','ID_ENT','ENTIDAD',
    #                                      'ID_MUN','MUNICIPIO','ID_LOCAL','LOCALIDAD','TOT_CASOS','Nombre_mod'])
    clues = clues.drop_duplicates(subset=['Clave_dh','Clave','UNIDAD','DELEGACIÓN','ID_ENT','ENTIDAD',
                                        'ID_MUN','MUNICIPIO','ID_LOCAL','LOCALIDAD','TOT_CASOS'])

    # No aseguramos que no tengamos filas vacias o que no haya datos faltantes
    # En este caso si tenemos datos faltantes 
    print("Verificamos que no tengamos unidades medicas sin su llave clue: " + str(clues['CLUES'].isnull().any()))

    # Nos aseguramos que la cantidad de Derechohabientes siga siendo la misma
    print("Verificamos que la cantidad de derechohabientes siga siendo igual " + str(clues['TOT_CASOS'].sum()))

    #clues_duplicados = clues[clues.duplicated(subset=["CLUES"],keep=False)]
    #clues_duplicados

    ############################################################################################################################################################
    #########################################################  Base Completa  ##################################################################################
    ############################################################################################################################################################


    clues_2 = pd.merge(DH_1, catalogo_b, left_on='Clave_dh',right_on='Clave_dh', how='left') 
    #clues_2.head(2)
    print("Ahora con la base completa la unimos la catálogo para agregarle el CLUE")


    # Dimensión con la base completa
    print("Verificamos la dimensión: " + str(clues_2.shape))

    print("verificamos que sean la misma cantidad de clues que con la base, reducida: " + str(len(clues_2['CLUES'].unique())))

    clues_expe = clues_2.copy()

    print(" Tenemos nulos:" + str(clues_expe['CLUES'].isnull().any()))

    print("Cantidad de derechohabientes para la base completa: " + str(clues_expe['TOT_CASOS'].sum()))

    del clues_expe["UNIDAD_y"]
    clues_expe = clues_expe.rename(columns={"UNIDAD_x":"UNIDAD"})

    if i=="2011" or i=="2012" or i=="2013" or i=="2014" or i == "2015" or i == "2016":
        clues_expe = clues_expe.drop_duplicates(subset=['ID_DELEG_RP_x','ID_SUBDEL_RP_x','ID_UMF_RP_x','Clave_dh','NOMBRE_UMF_RP',
                                                        'ST_TIT_FAM','ID_CALIDAD','CVE_GENERO','CVE_RANGO_EDAD','TOT_CASOS',
                                                        'DELEGACIÓN','UNIDAD','ID_ENT','ENTIDAD','ID_MUN','MUNICIPIO','ID_LOCAL','LOCALIDAD',
                                                        ])
    else:
        clues_expe = clues_expe.drop_duplicates(subset=['ID_DELEG_RP_x','ID_SUBDEL_RP_x','ID_UMF_RP_x','Clave_dh','NOMBRE_UMF_RP',
                                                        'ST_TIT_FAM','ID_CALIDAD','CVE_SEXO','CVE_RANGO_EDAD','TOT_CASOS',
                                                        'DELEGACIÓN','UNIDAD','ID_ENT','ENTIDAD','ID_MUN','MUNICIPIO','ID_LOCAL','LOCALIDAD',
                                                        ])
        
    print("Eliminamos duplicados en caso de haber")
    print("Volvemos a contar los derechohabientes: " + str(clues_expe['TOT_CASOS'].sum()))

    #clues_expe.shape

    #clues_expe['TOT_CASOS'].sum()

    with pd.ExcelWriter("Derechohabientes_" + i + "_" + claves[i][1:3] + ".xlsx") as writer:
        #clues_expe.to_excel(writer, sheet_name="Completo", index=False)
        clues.to_excel(writer, sheet_name="Unicos", index=False)

    print("Se creo archivo excel de derechohabientes: " + str(i) + "!!!!!!!!!")