import csv 
import matplotlib.pyplot as plt
import numpy as np
import math

def open_CTimages(rawpath,height,width):
	fd=open(rawpath,'rb')
	f=np.fromfile(fd,dtype=np.float32,count=height*width)
	return f,fd

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
	#平均、標準偏差を計算
	def calc_mean_std(self):
		self.mean=np.mean(self.mu)
		self.std=np.std(self.mu)

	#SNRを計算
	def calc_SNR(self):
		SNR=self.mean/self.std
		
		return SNR

if __name__=="__main__":
	width=height=512
	file_number=10000
	output_txtname='SNR_%d.csv' % file_number
	fig_name='SNR_%d.png' % file_number
	
	SNR_all=[]

	for i in range(file_number):
		i=i+1
		
		#インスタンスを作成
		snr=Calc_SNR(width,height)
		
		#再構成画像の置き場所
		rawpath="./Recon_{0}/FBP_virtual_projection_512x512_gammex{1}.raw".format(file_number,i)
		
		#画像をオープン
		f,fd=open_CTimages(rawpath,width,height)
		
		#Gammexのセンターのピクセルを取得
		snr.get_center_pixels(f)

		#平均、標準偏差を取得
		snr.calc_mean_std()

		#SNRを計算		
		SNR_value=snr.calc_SNR()

		#計算されたSNRを追加
		SNR_all.append(SNR_value)
	

	#textに保存
	np.savetxt(output_txtname,SNR_all,fmt='%.6f')
	
	#ここからはSNRをプロットして保存
	fig=plt.figure()	
	
	x=np.arange(1,file_number+1)

	plt.scatter(x,SNR_all,marker='^',s=10)
	
	plt.xlim([1,file_number])

	plt.xlabel('dataNo.')
	plt.ylabel('SNR')

	plt.title('SNR')
	
	plt.savefig(fig_name)
	
	plt.close()

