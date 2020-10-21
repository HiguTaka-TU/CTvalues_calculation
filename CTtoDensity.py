import matplotlib.pyplot as plt
import numpy as np
import csv

def CTtoDensityCurve_SB3_highest(csv_name):
	f1=np.loadtxt(csv_name,delimiter=',')
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



def CTtoDensity_NearestCurve(csv_name):
	f1=np.loadtxt(csv_name,delimiter=',')

	CT_values=np.array(f1)

	B3F =[-1006.4,-726.6,-560.5,-84.2,-40.3,-1.6,-2.5,21,63.9,203.8,219.1,598.3,1058.6,1581.3]
	QQ = [-1006.7,-704.3,-542.7,-94.4,-51.5,-13.3,-12.8,12.2,58.7,203,210.9,491.7,895.6,1338.3]
	New =[-1006.7,-706.9,-533,-94.4,-44.5,-3.5,-3.7,18.4,68.9,218.7,230.1,428,795.1,1246.6]

	B3F_nearest=1000000
	QQ_nearest=1000000
	New_nearest=1000000

	dif_B3F=np.sum(np.square(CT_values-B3F),axis=1)
	dif_QQ =np.sum(np.square(CT_values-QQ) ,axis=1)
	dif_New=np.sum(np.square(CT_values-New),axis=1)

	return np.argmin(dif_B3F),np.argmin(dif_QQ),np.argmin(dif_New)

