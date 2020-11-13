# -*- coding: utf-8 -*-
import csv 
import matplotlib.pyplot as plt
import numpy as np
import math

#MAEやRMSEなどの値を図にする
def evaluation_value_fig(save_name,title,csv_name,data):
	value=np.array(data)

	fig = plt.figure()
	x=np.arange(1500)
	plt.xlim([1,1500])
	plt.ylim([0,0.005])
	plt.scatter(x,value,c='blue',marker='^',s=50,alpha=0.7,linewidths='0')
	plt.title(title)
	plt.xlabel('testNo.')

	plt.savefig(save_name)
	plt.close()

#中央から5mm以内のピクセルを取得
def calc_SNR(f,width,height):
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

#一次元配列の平均、標準偏差を計算
def calc_mean_std(data)
	mean=np.mean(data)
	std=np.std(data)

	return mean,std

#SNRを無単位、[dB]の２通りで計算
def calc_SNR(mean,std)
	SNR1=10*math.log10(mean/std)
	SNR2=mean/std

	return SNR1,SNR2

#ノイズごとの平均エネルギーとSNRの関係をプロット
def SNR_meanenregy_fig(SNR,mean_energy,noise):
	label='noise %f' % noise
	fig=plt.figure()
	
	plt.scatter(MeanEnergy,SNR1,s=10,label='0.0000537')
	
	plt.xlabel('MeanEnergy')
	plt.ylabel('SNR')
	
	plt.title('SNR-MeanEnergy')
	plt.legend(loc='upper left')
	filename='SNR-MeanEnergy_Noise.png'
	plt.savefig(filename)
	plt.close()

if __name__=="__main__":
	Check_SNR_MeanEnergy()
