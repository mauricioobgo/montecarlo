#################################################################################################################
#Modelo de Montecarlo con acciones.
#ELaborado por Mauricio Obando
#Este script asume que se preinstalo debidamente el api de yahooFinance, el instructivo lo puede encontrar en 
#https://pypi.python.org/pypi/yahoo-finance
#################################################################################################################

import yahoo_finance as yahoo
import numpy as np
import pandas as pds
import datetime

#Instanciar el valor de un acción en este caso Apple
valueStockPrice=yahoo.Share('AAPL')
#arreglo de históricos
#fecha actual
actualDate=datetime.datetime.now()
#fecha -20 días
pastDate=actualDate+datetime.timedelta(days=-20)
print(actualDate,"Fecha Actual")
print(pastDate,"Fecha -20 días")
#convertir fechas en strings
actualDate=datetime.datetime.strftime(actualDate,"%Y-%m-%d")
pastDate=datetime.datetime.strftime(pastDate,"%Y-%m-%d")
#arreglo con información
dataFrameHist=pds.DataFrame.from_dict(valueStockPrice.get_historical(pastDate,actualDate))
print(dataFrameHist)