# -*- coding: iso-8859-1 -*-

import random

studentenK = ["Brian Ceccato","Tobias Wyss","Jael Kaeser","Naemi Hari","Mathias Inniger","Mireille Wettstein","Marc Wettstein"]
studentenV = ["Sabrina Cookman","Vanessa Batifu","Bettina Willen","Deborah Hersche","Pascal Schaedeli","Stephan Walz","Benjamin Willen","Milena Kuhlmann","Renate Stucki","Kerstin Perren","Andrina Isliker","Julia Baumann","Salomon Hersche"]

for kalenderwoche in range(33, 53):

	random.shuffle(studentenK)
	random.shuffle(studentenV)
	
	gebetsteams = [
		studentenK[0]+" / "+studentenK[1],
		studentenK[2]+" / "+studentenK[3],
		studentenK[4]+" / "+studentenK[5]+" / "+studentenK[6],
		studentenV[0]+" / "+studentenV[1],
		studentenV[2]+" / "+studentenV[3],
		studentenV[4]+" / "+studentenV[5]+" / "+studentenV[6],
		studentenV[7]+" / "+studentenV[8]+" / "+studentenV[9],
		studentenV[10]+" / "+studentenV[11]+" / "+studentenV[12]
		]
	
	random.shuffle(gebetsteams)
	
	print ("-----Gebetsplan für Woche "+str(kalenderwoche)+"-----")
	print ("23:00 - 00:00 | "+gebetsteams[0])
	print ("00:00 - 01:00 | "+gebetsteams[1])
	print ("01:00 - 02:00 | "+gebetsteams[2])
	print ("02:00 - 03:00 | "+gebetsteams[3])
	print ("03:00 - 04:00 | "+gebetsteams[4])
	print ("04:00 - 05:00 | "+gebetsteams[5])
	print ("05:00 - 06:00 | "+gebetsteams[6])
	print ("06:00 - 07:00 | "+gebetsteams[7])
	print ("")