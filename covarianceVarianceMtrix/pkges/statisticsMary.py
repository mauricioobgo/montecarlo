# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:19:34 2016

@author: mauricio
"""

import numpy as np
import math

class statsGeneral:
    
    def correlationMatrix(arrayN):
        
        c = np.array(arrayN)
        
        cm =np.corrcoef(c)
        
        return cm
        

#tickersCorr = ["ABC","XYZ"]
#tdv = {"ABC":0.3,"XYZ":0.2}
#ickersCorr = ["ABC","XYZ"]
    def varCovarMatrix(stocksInPortfolio,coorelations,stdv,tickersCorr):
        new = np.array(coorelations)
        vcv = []
        for eachStock in stocksInPortfolio:
            row = []
            for ticker in stocksInPortfolio:
                if eachStock == ticker:
                    variance = math.pow(stdv[ticker],2)
                    row.append(variance)
                else:
                    cov = stdv[ticker]*stdv[eachStock]* new[tickersCorr.index(ticker)][tickersCorr.index(eachStock)]
                    row.append(cov)
            vcv.append(row)
    
        vcvmat = np.mat(vcv)
    
        return vcvmat
        

