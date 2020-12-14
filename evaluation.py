# -*- coding: utf-8 -*-
import csv 
import matplotlib.pyplot as plt
import numpy as np
import math

#RMSEなどの値を図にする
def evaluation_value_fig(fig_name,title,data):
	value=np.array(data)

	fig = plt.figure()
	
	x=np.arange(1,test_size+1)
	
	plt.xlim([1,test_size])

	plt.scatter(x,value,c='blue',marker='^',s=50,alpha=0.7,linewidths='0')
	plt.title(title)
	plt.xlabel('testNo.')

	plt.savefig(fig_name)
	plt.close()


if __name__=="__main__":
	"""	
	#rmseの図示を行う
	rmse=np.loadtxt('../DNN/rmse/rmse_10000.csv')
	evaluation_value_fig('rmse_10000.png','rmse',rmse)	
	"""
	
