# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt
import csv

#GammexファントムのCT画像から各インサートのCT値を計算するクラス
class CTvalues():
	PI=math.pi
	r0=55
	r00=105
	r000=180
		
	def __init__(self,inner_insert_number,outer_insert_number):
		self.inner_insert_number=inner_insert_number
		self.outer_insert_number=outer_insert_number
		self.theta=[]
		self.x=[]
		self.y=[]
		self.distance=[0]*14
		self.sum=[0]*14
		self.count=[0]*14
		self.average=[0]*14
		self.ct=[]


	#角度を計算
	def calc_inner_theta(self,insert_number):
		self.theta.append(45*insert_number*CTvalues.PI/180)

	def calc_outer_theta(self,insert_number):
		self.theta.append((45/2+45*insert_number)*CTvalues.PI/180)
	
	#座標を計算
	def calc_inner_coordinate(self,theta):
		self.x.append(CTvalues.r0*math.cos(theta))
		self.y.append(CTvalues.r0*math.sin(theta))
	
	def calc_outer_coordinate(self,theta):
		self.x.append(CTvalues.r00*math.cos(theta))
		self.y.append(CTvalues.r00*math.sin(theta))

	def calc_air_coordinate(self):
		self.x.append(CTvalues.r000*math.sin(0))
		self.y.append(CTvalues.r000*math.cos(0))
	
	#該当するインサートのCT値の合計とカウントを計算
	def calc_sum_and_count(self):	
		for iy in range(height):
			Y =-iy+height/2-0.5
			for ix in range(width):
				X=ix-width/2+0.5
				for k in range(14):
					self.distance[k]=(X-self.x[k])*(X-self.x[k])+(Y-self.y[k])*(Y-self.y[k])
					if self.distance[k]<=25:
						self.sum[k]+=f[ix+iy*width]
						self.count[k]+=1
	#CT値の計算        
	def calc_ctvalues(self):   
		for i in range(14):                                                                    
			self.average[i]=self.sum[i]/self.count[i]
		
		for i in range(14):
			self.ct.append((self.average[i]-self.average[4])/self.average[4]*1000)

		return self.ct[13],self.ct[8],self.ct[9],self.ct[0],self.ct[3],self.ct[4],self.ct[7],self.ct[1],self.ct[11],self.ct[12],self.ct[10],self.ct[5],self.ct[6],self.ct[2]

def open_CTimages(rawpath,height,width):
	fd=open(rawpath,'rb')
	f=np.fromfile(fd,dtype=np.float32,count=height*width)
	return f,fd

def convert_CTvalue(f,fd,mu_water,output_name):
	for j in range(height*width):
		f[j]=(f[j]-mu_water)/mu_water*1000

	f.tofile(output_name)

def main():	
	#インサートの番号を入力
	inner_insert_number=[0,1,2,3,4,5,7]
	outer_insert_number=[2,1,3,4,5,7]
	
	#インスタンスを生成
	ctvalues=CTvalues(inner_insert_number,outer_insert_number)
	
	#各インサートの角度を計算
	for number in inner_insert_number:
		ctvalues.calc_inner_theta(number)

	for number in outer_insert_number:
		ctvalues.calc_outer_theta(number)
	
	#各インサートの座標を計算
	for number in range(len(inner_insert_number)):
		ctvalues.calc_inner_coordinate(ctvalues.theta[number])
	
	for number in range(len(inner_insert_number),len(inner_insert_number)+len(outer_insert_number)):
		ctvalues.calc_outer_coordinate(ctvalues.theta[number])
	
	ctvalues.calc_air_coordinate()

	#各インサートの減弱係数の合計とカウントを計算
	ctvalues.calc_sum_and_count()

	#各インサートのCT値を計算
	ctvalues14=ctvalues.calc_ctvalues()

	return ctvalues.average[4],ctvalues14

if __name__=="__main__":
	width=height=512
	data_size=10000
	csv_outname='CTvalues_%d.csv' % data_size

	#CT画像に変換して保存したいときに'True'をセット
	convert='False'

	for i in range(data_size):
		i=i+1
		rawpath='./Recon_{0}/FBP_virtual_projection_512x512_gammex{1}.raw'.format(data_size,i)
		
		f,fd=open_CTimages(rawpath,height,width)
		mu_water,ctvalues14=main()
		
		with open(csv_outname,'a') as file_csv:
				writer=csv.writer(file_csv)
				writer.writerow(ctvalues14)
		
		if convert=='True':
			output_name='CTimages/CT_images%d.raw' % i
			convert_CTvalue(f,fd,mu_water,output_name)
		fd.close()
