import csv 
import matplotlib.pyplot as plt
import numpy as np

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

def SNR(f):
        mu=[]
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
        SNR=10*math.log10(mean/std)
