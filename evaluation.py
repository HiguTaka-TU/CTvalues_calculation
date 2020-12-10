# -*- coding: utf-8 -*-
import csv 
import matplotlib.pyplot as plt
import numpy as np
import math

import CTvalues

#MAEやRMSEなどの値を図にする
def evaluation_value_fig(save_name,title,data):
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


class Calc_SNR(): 
	def __init__(self,width,height):
		self.width=width
		self.height=height

		self.mu=[]
		self.sum_mu=0
		self.sum_count=0

		self.mean=0
		self.std=0
	#中央から5mm以内にあるピクセルを取得する
	def get_center_pixels(self,f):
		
		for iy in range(self.height):
			y =-iy+self.height/2-0.5
			for ix in range(self.width):
				x=ix-self.width/2+0.5
				d=x*x+y*y  
				if d<=25:
					self.mu.append(f[ix+iy*width])
	#一次元配列の平均、標準偏差を計算
	def calc_mean_std(self):
		self.mean=np.mean(self.mu)
		self.std=np.std(self.mu)

	#SNRを無単位、[dB]の２通りで計算
	def calc_SNR(self):
		#SNR1=10*math.log10(mean/std)
		SNR=self.mean/self.std
		
		return SNR



#ノイズごとの平均エネルギーとSNRの関係をプロット
def SNR_meanenregy_fig(SNR,mean_energy,noise):
	label='noise %f' % noise
	
	plt.scatter(mean_energy,SNR,color='blue',s=10,label='{0:.5f}'.format(noise))
	
	plt.xlabel('MeanEnergy')
	plt.ylabel('SNR')
	

if __name__=="__main__":
	width=height=512
	file_number=570
	SNR_all=[]
	for i in range(file_number):
		calc_SNR=Calc_SNR(width,height)
		i=i+1
		rawpath="/workspace/Ver.2_FBP_FromVirtualProjection/Recon_noise0.00001/FBP_virtual_projection_512x512_gammex%d.raw" % i
		f,fd=CTvalues.open_CTimages(rawpath,width,height)
		calc_SNR.get_center_pixels(f)
		calc_SNR.calc_mean_std()
		SNR=calc_SNR.calc_SNR()
		SNR_all.append(SNR)
	
	np.savetxt('SNR_noise/check/noise0.00001.csv',SNR_all,fmt='%.6f')
	
	"""
	#SNRの計算を行い、ファイルに保存
	SNR=[]
	for i in range(570):
		i = i+1
		rawpath="/workspace/Ver.2_FBP_FromVirtualProjection/Recon_noise0.00001/FBP_virtual_projection_512x512_gammex%d.raw" % i
		f,fd=CTvalues.open_CTimages(rawpath,width,height)
		mu=get_center_pixels(f,width,height)
		mean,std=calc_mean_std(mu)
		SNR=calc_SNR(mean,std)
		SNR.append(SNR2)
		fd.close()
	np.savetxt('SNR_noise/check/noise0.00001.csv',SNR,fmt='%.6f')
	"""
	"""
	rmse=np.loadtxt('../DNN/rmse/rmse_10000.csv')
	evaluation_value_fig('rmse_10000.png','rmse',rmse)	
	"""	

	"""
	#ノイズごとのSNRをグラフにする
	SNR1=np.loadtxt('SNR_noise/check/noise0.0001.csv',delimiter=',')
	SNR2=np.loadtxt('SNR_noise/check/noise0.00005.csv',delimiter=',')
	SNR3=np.loadtxt('SNR_noise/check/noise0.00001.csv',delimiter=',')
	

	mean_energy=np.loadtxt('../spectrum/mean_energy_file/check/check_mean_energy.csv',delimiter=',')

	fig=plt.figure()
	
	SNR_meanenregy_fig(SNR1,mean_energy,0.0001)
	SNR_meanenregy_fig(SNR2,mean_energy,0.00005)
	SNR_meanenregy_fig(SNR3,mean_energy,0.00001)
	
	plt.title('SNR-MeanEnergy')
	plt.legend(loc='upper left')
	filename='SNR-MeanEnergy_Noise.png'
	plt.savefig(filename)
	plt.close()
	"""		
