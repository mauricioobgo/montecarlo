# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:39:42 2016

@author: mauricio
"""
from managerFlat import flatManager as flat

def main():
	
	try:
		print("prueba")
		felix=flat()
		felix.frameImport()
		#felix=sq("nuevaM")
		#,lfelix.nuevaPrueba()
		
		

	except(ValueError,TypeError):
		print("an error ocurred")
	
if __name__=="__main__":
	main()
	