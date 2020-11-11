import csv 
import matplotlib.pyplot as plt
import numpy as np
import math

def MAE_fig(csv_name):
	f1=np.loadtxt(csv_name,delimiter=',')
	MAE=np.array(f1)

	fig = plt.figure()
	x=np.arange(1500)
	plt.xlim([1,1500])
	plt.ylim([0,0.005])
	plt.scatter(x,MAE,c='blue',marker='^',s=50,alpha=0.7,linewidths='0')
	plt.title('MAE')
	plt.xlabel('testNo.')
	filename='./MAE.png'
	plt.savefig(filename)
	plt.close()

def RMSE_fig(csv_name):
	f1=np.loadtxt(csv_name,delimiter=',')
	RMSE=np.array(f1)

	fig = plt.figure()
	x=np.arange(1500)
	plt.xlim([1,1500])
	plt.ylim([0,0.005])
	plt.scatter(x,RMSE,c='blue',marker='^',s=50,alpha=0.7,linewidths='0')
	plt.title('RMSE')
	plt.xlabel('testNo.')
	filename='./RMSE.png'
	plt.savefig(filename)
	plt.close()

def SNR(f,width,height):
	mu=[]
	SNR1_all=[]
	SNR2_all=[]
	sum_mu=0
	sum_count=0 
	for iy in range(height):
		y =-iy+height/2-0.5
		for ix in range(width):
			x=ix-width/2+0.5
			d=x*x+y*y 
    
			if d<=25:
				mu.append(f[ix+iy*width])
	mean=np.mean(mu)
	std=np.std(mu)
	SNR1=10*math.log10(mean/std)
	SNR2=mean/std

	SNR1_all.append(SNR1)
	SNR2_all.append(SNR2)

	return SNR1_all,SNR2_all

def Check_SNR_MeanEnergy():
	SNR_file1='SNR7500.csv'
	#SNR_file2='SNR_Noise0.0002.csv'
	#SNR_file3='SNR_Noise0.0003.csv'
	#SNR_file4='SNR_Noise0.0004.csv'
	#SNR_file5='SNR_Noise0.0005.csv'
	#SNR_file6='SNR_Noise0.0006.csv'
	#SNR_file7='SNR_Noise0.0007.csv'
	#SNR_file8='SNR_Noise0.0008.csv'
	#SNR_file9='SNR_Noise0.0009.csv'
	MeanEnergy_file='MeanEnergy7500.csv'
	

	SNR1=np.loadtxt(SNR_file1,delimiter=',')	
	#SNR2=np.loadtxt(SNR_file2,delimiter=',')	
	#SNR3=np.loadtxt(SNR_file3,delimiter=',')	
	#SNR4=np.loadtxt(SNR_file4,delimiter=',')	
	#SNR5=np.loadtxt(SNR_file5,delimiter=',')	
	#SNR6=np.loadtxt(SNR_file6,delimiter=',')	
	#SNR7=np.loadtxt(SNR_file7,delimiter=',')	
	#SNR8=np.loadtxt(SNR_file8,delimiter=',')	
	#SNR9=np.loadtxt(SNR_file9,delimiter=',')	
	MeanEnergy=np.loadtxt(MeanEnergy_file,delimiter=',')	

	fig=plt.figure()
	
	
	plt.scatter(MeanEnergy,SNR1,s=10,label='0.0000537')
	#plt.scatter(MeanEnergy,SNR2,s=10,label='0.0002')
	#plt.scatter(MeanEnergy,SNR3,s=10,label='0.0003')
	#plt.scatter(MeanEnergy,SNR4,s=10,label='0.0004')
	#plt.scatter(MeanEnergy,SNR5,s=10,label='0.0005')
	#plt.scatter(MeanEnergy,SNR6,s=10,label='0.0006')
	#plt.scatter(MeanEnergy,SNR7,s=10,label='0.0007')
	#plt.scatter(MeanEnergy,SNR8,s=10,label='0.0008')
	#plt.scatter(MeanEnergy,SNR9,s=10,label='0.0009')
	
	plt.xlabel('MeanEnergy')
	plt.ylabel('SNR')
	
	plt.title('SNR-MeanEnergy')
	plt.legend(loc='upper left')
	filename='SNR-MeanEnergy_Noise.png'
	plt.savefig(filename)
	plt.close()

Check_SNR_MeanEnergy()
