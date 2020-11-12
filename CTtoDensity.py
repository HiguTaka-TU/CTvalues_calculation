# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import csv

def definition_density()
	density=[0.002,0.28,0.40,0.942,0.977,1.0,1.018,1.053,1.097,1.143,1.154,1.335,1.56,1.825]
	density_actual=[0,0.3,0.48,0.949,0.984,1,1.016,1.018,1.051,1.09,1.138,1.146,1.333,1.56,1.822]
	
	return density,density

def actual_CTvalues()
	B3F =[-1006.4,-726.6,-560.5,-84.2,-40.3,-1.6,-2.5,21,63.9,203.8,219.1,598.3,1058.6,1581.3]
	QQ = [-1006.7,-704.3,-542.7,-94.4,-51.5,-13.3,-12.8,12.2,58.7,203,210.9,491.7,895.6,1338.3]
	New =[-1006.7,-706.9,-533,-94.4,-44.5,-3.5,-3.7,18.4,68.9,218.7,230.1,428,795.1,1246.6]
	
	return B3F,QQ,New

def CT_ED_SB3_highest(data):
	CT_values=np.array(data)
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


#実測のカーブと最も近いデータセットのカーブの番号を出力
def CT_ED_nearest(data):
	CT_values=np.array(data)

	B3F_nearest=1000000000
	QQ_nearest=1000000000
	New_nearest=1000000000

	dif_B3F=np.sum(np.square(CT_values-B3F),axis=1)
	dif_QQ =np.sum(np.square(CT_values-QQ) ,axis=1)
	dif_New=np.sum(np.square(CT_values-New),axis=1)

	return np.argmin(dif_B3F),np.argmin(dif_QQ),np.argmin(dif_New)

def CTtoDensity_actual_fig():
	"""
	ax = fig.add_subplot(111)
	
	ax.spines['left'].set_position(('data',0))
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	"""

	
	#fig=plt.figure()
	

	plt.scatter(B3F,density_actual,marker="^",s=10,color='blue',label='B3F')
	plt.scatter(QQ,density_actual,marker="^",s=10,color='red',label='QQ')
	plt.scatter(New,density_actual,marker="^",s=10,color='green',label='New')
	
	plt.title('CTtoDensity Curve')
	plt.legend(loc='lower right')        
	#filename='./CTtoDensity_actual.png'
	#plt.savefig(filename)
	#plt.close()

def CTtoDensity_fig(csv_name):
	ax = fig.add_subplot(111)
	
	ax.spines['left'].set_position(('data',0))
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	
	f1=np.loadtxt(csv_name,delimiter=',')
	CT_number=np.array(f1)
	
	
	for i in range(CT_number.shape[0]):
		if i==1:
			plt.scatter(CT_number[i,:],density,marker="^",s=10,alpha=0.5,color='Cyan',label='Dataset')
		else:
			plt.scatter(CT_number[i,:],density,marker="^",s=10,alpha=0.5,color='Cyan')
	
def interpolation_fig(data):
	"""
	ax = fig.add_subplot(111)
	
	ax.spines['left'].set_position(('data',0))
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	"""
	CT_number=np.array(data)
	plt.scatter(CT_number[0,:],density,marker="^",s=10,color='blue',label='B3F')
	plt.scatter(CT_number[1,:],density,marker="^",s=10,color='red',label='QQ')
	plt.scatter(CT_number[2,:],density,marker="^",s=10,color='green',label='New')
	

def interpolation():
	delta_x_B3F=np.empty(len(density)-1)
	delta_x_QQ=np.empty(len(density)-1)
	delta_x_New=np.empty(len(density)-1)
	delta_y=np.empty(len(density)-1)
	
	slope_B3F=np.empty(len(density)-1)
	slope_QQ=np.empty(len(density)-1)
	slope_New=np.empty(len(density)-1)

	intercept_B3F=np.empty(len(density)-1)
	intercept_QQ=np.empty(len(density)-1)
	intercept_New=np.empty(len(density)-1)

	B3F_Interpolation=np.empty(len(density))
	QQ_Interpolation=np.empty(len(density))
	New_Interpolation=np.empty(len(density))
	
	for i in range(len(density)-1):
		delta_x_B3F[i]=B3F[i+1]-B3F[i]
		delta_x_QQ[i]=QQ[i+1]-QQ[i]
		delta_x_New[i]=New[i+1]-New[i]
		delta_y[i]=density_actual[i+1]-density_actual[i]
	
		slope_B3F[i]=delta_y[i]/delta_x_B3F[i]
		slope_QQ[i]=delta_y[i]/delta_x_QQ[i]
		slope_New[i]=delta_y[i]/delta_x_New[i]

		intercept_B3F[i]=density_actual[i]-slope_B3F[i]*B3F[i]
		intercept_QQ[i]=density_actual[i]-slope_QQ[i]*QQ[i]
		intercept_New[i]=density_actual[i]-slope_New[i]*New[i]

	for i in range(0,2):
		B3F_Interpolation[i]=1/slope_B3F[0]*(density[i]-intercept_B3F[0])
		QQ_Interpolation[i]=1/slope_QQ[0]*(density[i]-intercept_QQ[0])
		New_Interpolation[i]=1/slope_New[0]*(density[i]-intercept_New[0])
	for i in range(2,5):
		B3F_Interpolation[i]=1/slope_B3F[i-1]*(density[i]-intercept_B3F[i-1])
		QQ_Interpolation[i]=1/slope_QQ[i-1]*(density[i]-intercept_QQ[i-1])
		New_Interpolation[i]=1/slope_New[i-1]*(density[i]-intercept_New[i-1])
	for i in range(5,7):
		B3F_Interpolation[i]=B3F[i]
		QQ_Interpolation[i]=QQ[i]
		New_Interpolation[i]=New[i]	
	for i in range(7,12):
		B3F_Interpolation[i]=1/slope_B3F[i]*(density[i]-intercept_B3F[i])
		QQ_Interpolation[i]=1/slope_QQ[i]*(density[i]-intercept_QQ[i])
		New_Interpolation[i]=1/slope_New[i]*(density[i]-intercept_New[i])
	for i in range(12,13):
		B3F_Interpolation[i]=B3F[i]
		QQ_Interpolation[i]=QQ[i]
		New_Interpolation[i]=New[i]
	for i in range(13,14):
		B3F_Interpolation[i]=1/slope_B3F[i-1]*(density[i]-intercept_B3F[i-1])
		QQ_Interpolation[i]=1/slope_QQ[i-1]*(density[i]-intercept_QQ[i-1])
		New_Interpolation[i]=1/slope_New[i-1]*(density[i]-intercept_New[i-1])
	
	with open('Interpolation.csv','a') as f:
		writer=csv.writer(f)
		writer.writerow(B3F_Interpolation)
		writer.writerow(QQ_Interpolation)
		writer.writerow(New_Interpolation)
		
def feature_fig(csv_name,i):
	f1=np.loadtxt(csv_name,delimiter=',')
	CTvalues=np.array(f1)
	
	f2=np.loadtxt('Interpolation.csv',delimiter=',')
	CTvalues_actual=np.array(f2)

	fig=plt.figure()
	x=np.arange(1,7501,1)
	plt.scatter(x,CTvalues[:,i],marker='^',s=5,label='Dataset')
	
	plt.legend(loc='upper right')        
	filename='feature_value_%d.png' % i
	plt.savefig(filename)
	plt.close()
		

"""
fig = plt.figure()
CTtoDensity_fig('CTnumber7500.csv')
CTtoDensity_Interpolation_fig('Interpolation.csv')
#CTtoDensity_actual_fig()
plt.title('CTtoDensity Curve')
plt.legend(loc='lower right')        
filename='./CTtoDensity.png'
plt.savefig(filename)
plt.close()
"""
i=0
feature_fig('CTnumber7500.csv',i)
