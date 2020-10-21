import matplotlib.pyplot as plt
import numpy as np
import csv

def CTtoDensityCurve_SB3_highest(csv1_name):
	#csv1_name = './CTvalue_Noise0.0001.csv'
	f1=np.loadtxt(csv1_name,delimiter=',')
	CT_number=np.array(f1)

	density=[0.002,0.28,0.40,0.942,0.977,1.0,1.018,1.053,1.097,1.143,1.154,1.335,1.56,1.825]
	#global CT_max
	CT_max=0
	fig = plt.figure()
	for i in range(0,570):
		if CT_number[i,13]>CT_max:
			CT_max=CT_number[i,13]
			print(i)
			max=i
	plt.plot(CT_number[max],density,marker="^",color='green')
	filename='./CTtoDensity.png'
	plt.savefig(filename)
	plt.close()
