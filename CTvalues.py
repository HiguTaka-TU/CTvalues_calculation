import numpy as np
import math
import matplotlib.pyplot as plt
import csv

CT1=0
CT2=0
CT3=0
CT4=0
CT5=0
CT6=0
CT7=0
CT8=0
CT9=0
CT10=0
CT11=0
CT12=0
CT13=0
CT14=0
CT15=0
CT16=0
CTAir=0

width=512
height=512

def CTnumber():
	PI=math.pi
	r0=55
	r00=105
	r000=180

	theta1=(45/2+45*2)*PI/180
	x1=r00*math.cos(theta1)
	y1=r00*math.sin(theta1)
	theta2=(45/2+45*1)*PI/180
	x2=r00*math.cos(theta2)
	y2=r00*math.sin(theta2)

	theta3=(45/2+45*0)*PI/180
	x3=r00*math.cos(theta3)   
	y3=r00*math.sin(theta3)

	theta4=(45/2+45*(-1))*PI/180
	x4=r00*math.cos(theta4)
	y4=r00*math.sin(theta4)

	theta5=(45/2+45*(-2))*PI/180
	x5=r00*math.cos(theta5)
	y5=r00*math.sin(theta5)

	theta6=(45/2+45*(-3))*PI/180
	x6=r00*math.cos(theta6)
	y6=r00*math.sin(theta6)

	theta7=(45/2+45*(-4))*PI/180
	x7=r00*math.cos(theta7)
	y7=r00*math.sin(theta7)

	theta8=(45/2+45*(-5))*PI/180
	x8=r00*math.cos(theta8)
	y8=r00*math.sin(theta8)

	theta9=45*2*PI/180
	x9=r0*math.cos(theta9)
	y9=r0*math.sin(theta9)

	theta10=45*1*PI/180
	x10=r0*math.cos(theta10)
	y10=r0*math.sin(theta10)

	theta11=45*0*PI/180
	x11=r0*math.cos(theta11)
	y11=r0*math.sin(theta11)

	theta12=45*(-1)*PI/180
	x12=r0*math.cos(theta12)
	y12=r0*math.sin(theta12)

	theta13=45*(-2)*PI/180
	x13=r0*math.cos(theta13)
	y13=r0*math.sin(theta13)

	theta14=45*(-3)*PI/180
	x14=r0*math.cos(theta14)
	y14=r0*math.sin(theta14)

	theta15=45*(-4)*PI/180
	x15=r0*math.cos(theta15)
	y15=r0*math.sin(theta15)

	theta16=45*(-5)*PI/180
	x16=r0*math.cos(theta16)
	y16=r0*math.sin(theta16)

	#Air Angle=0
	xAir=r000*math.sin(theta11)
	yAir=r000*math.cos(theta11)

	#print(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16)
	#print(y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16)

	#sum of mu for average
	sum1mu=0
	sum2mu=0
	sum3mu=0
	sum4mu=0
	sum5mu=0
	sum6mu=0
	sum7mu=0
	sum8mu=0
	sum9mu=0
	sum10mu=0
	sum11mu=0
	sum12mu=0
	sum13mu=0
        sum14mu=0
        sum15mu=0
        sum16mu=0
        sumAirmu=0

        #sum of pixel for average
        sum1count=0
        sum2count=0
        sum3count=0
        sum4count=0
        sum5count=0
        sum6count=0
        sum7count=0
        sum8count=0
        sum9count=0
        sum10count=0
        sum11count=0
        sum12count=0
        sum13count=0
        sum14count=0
        sum15count=0
        sum16count=0
        sumAircount=0

        #average of mu
        ave1=0
        ave2=0
        ave3=0
        ave4=0
        ave5=0
        ave6=0
        ave7=0
        ave8=0
        ave9=0
        ave10=0
        ave11=0
        ave12=0
        ave13=0
        ave14=0
        ave15=0
        ave16=0
        aveAir=0

        for iy in range(height):
                y =-iy+height/2-0.5
                for ix in range(width):
                        x=ix-width/2+0.5
                        d1=(x-x1)*(x-x1)+(y-y1)*(y-y1)
                        d2=(x-x2)*(x-x2)+(y-y2)*(y-y2)
                        d3=(x-x3)*(x-x3)+(y-y3)*(y-y3)
                        d4=(x-x4)*(x-x4)+(y-y4)*(y-y4)
                        d5=(x-x5)*(x-x5)+(y-y5)*(y-y5)
                        d6=(x-x6)*(x-x6)+(y-y6)*(y-y6)
                        d7=(x-x7)*(x-x7)+(y-y7)*(y-y7)
                        d8=(x-x8)*(x-x8)+(y-y8)*(y-y8)
                        d9=(x-x9)*(x-x9)+(y-y9)*(y-y9)
                        d10=(x-x10)*(x-x10)+(y-y10)*(y-y10)
                        d11=(x-x11)*(x-x11)+(y-y11)*(y-y11)
                        d12=(x-x12)*(x-x12)+(y-y12)*(y-y12)
                        d13=(x-x13)*(x-x13)+(y-y13)*(y-y13)
                        d14=(x-x14)*(x-x14)+(y-y14)*(y-y14)
                        d15=(x-x15)*(x-x15)+(y-y15)*(y-y15)
                        d16=(x-x16)*(x-x16)+(y-y16)*(y-y16)
                        dAir=(x-xAir)*(x-xAir)+(y-yAir)*(y-yAir)

                        if d1<=25:
                                #print(f[width*iy+ix])
                                sum1mu+=f[ix+iy*width]
                                sum1count+=1
                        elif d2<=25:
                                #print(f[width*iy+ix])
                                sum2mu+=f[ix+iy*width]
                                sum2count+=1
                        elif d3<=25:
                                #print(f[width*iy+ix])
                                sum3mu+=f[ix+iy*width]
                                sum3count+=1
                        elif d4<=25:
                                #print(f[width*iy+ix])
                                sum4mu+=f[ix+iy*width]
                                sum4count+=1
                        elif d5<=25:
                                #print(f[width*iy+ix])
                                sum5mu+=f[ix+iy*width]
                                sum5count+=1
                        elif d6<=25:
                                #print(f[width*iy+ix])
                                sum6mu+=f[ix+iy*width]
                                sum6count+=1
                        elif d7<=25:
                                #print(f[width*iy+ix])
                                sum7mu+=f[ix+iy*width]
                                sum7count+=1
                        elif d8<=25:
                                #print(f[width*iy+ix])
                                sum8mu+=f[ix+iy*width]
                                sum8count+=1
                        elif d9<=25:
                                #print(f[width*iy+ix])
                                sum9mu+=f[ix+iy*width]
                                sum9count+=1
                        elif d10<=25:
                                #print(f[width*iy+ix])
                                sum10mu+=f[ix+iy*width]
                                sum10count+=1
                        elif d11<=25:
                                #print(f[width*iy+ix])
                                sum11mu+=f[ix+iy*width]
                                sum11count+=1
                        elif d12<=25:
                                #print(f[width*iy+ix])
                                sum12mu+=f[ix+iy*width]
                                sum12count+=1
                        elif d13<=25:
                                #print(f[width*iy+ix])
                                sum13mu+=f[ix+iy*width]
                                sum13count+=1
                        elif d14<=25:
                                #print(f[width*iy+ix])
                                sum14mu+=f[ix+iy*width]
                                sum14count+=1
                        elif d15<=25:
                                #print(f[width*iy+ix])
                                sum15mu+=f[ix+iy*width]
                                sum15count+=1
                        elif d16<=25:
                                #print(f[width*iy+ix])
                                sum16mu+=f[ix+iy*width]
                                sum16count+=1
                        elif dAir<=25:
                                #print(f[width*iy+ix])
                                sumAirmu+=f[ix+iy*width]
                                sumAircount+=1
                                                                               
                                fd.close()
	print(sum3count)
	print(sum4count)
        #calculate average
        ave1=sum1mu/sum1count
        ave2=sum2mu/sum2count
        ave3=sum3mu/sum3count
        ave4=sum4mu/sum4count
        ave5=sum5mu/sum5count
        ave6=sum6mu/sum6count
        ave7=sum7mu/sum7count
        ave8=sum8mu/sum8count
        ave9=sum9mu/sum9count
        ave10=sum10mu/sum10count
        ave11=sum11mu/sum11count
        ave12=sum12mu/sum12count
        ave13=sum13mu/sum13count
        ave14=sum14mu/sum14count
        ave15=sum15mu/sum15count
        ave16=sum16mu/sum16count
        aveAir=sumAirmu/sumAircount

        global CT1
	CT1=(ave1-ave15)/ave15*1000#Solid water
        global CT2
	CT2=(ave2-ave15)/ave15*1000#LN300
        global CT3
	CT3=(ave3-ave15)/ave15*1000#Solid water
        global CT4
	CT4=(ave4-ave15)/ave15*1000#IB3
	global CT5
        CT5=(ave5-ave15)/ave15*1000#Solid water
	global CT6
        CT6=(ave6-ave15)/ave15*1000#LV1
	global CT7
        CT7=(ave7-ave15)/ave15*1000#B200
	global CT8
        CT8=(ave8-ave15)/ave15*1000#LN450
	global CT9
        CT9=(ave9-ave15)/ave15*1000#SB3-Cortical
	global CT10
        CT10=(ave10-ave15)/ave15*1000#SR2-Brain
	global CT11
        CT11=(ave11-ave15)/ave15*1000#AP6
	global CT12
        CT12=(ave12-ave15)/ave15*1000#CB2-50%
	global CT13
        CT13=(ave13-ave15)/ave15*1000#Solid water
	global CT14
        CT14=(ave14-ave15)/ave15*1000#CB2-30%
	global CT15
        CT15=(ave15-ave15)/ave15*1000#Water
	global CT16
        CT16=(ave16-ave15)/ave15*1000#BR12
	global CTAir
        CTAir=(aveAir-ave15)/ave15*1000#Air

"""
rawpath="/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/Ver.2_FBP_FromVirtualProjection/Reconstruction/FBP_virtual_projection_512x512_gammex1.raw" 
fd=open(rawpath,'rb')
f=np.fromfile(fd,dtype=np.float32,count=height*width)
#img=f.reshape((height,width))
CTnumber()
"""


for i in range(1,7501):
#for i in range(1,2):
	rawpath="/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/Ver.2_FBP_FromVirtualProjection/Reconstruction/FBP_virtual_projection_512x512_gammex%d.raw" % i 
	fd=open(rawpath,'rb')
	f=np.fromfile(fd,dtype=np.float32,count=height*width)
	#img=f.reshape((height,width))
	CTnumber()
	with open('CTnumber_abs.csv','a') as f:
		writer=csv.writer(f)
		writer.writerow([abs(CTAir),abs(CT2),abs(CT8),abs(CT11),abs(CT16),abs(CT15),abs(CT1),abs(CT10),abs(CT6),abs(CT4),abs(CT7),abs(CT14),abs(CT12),abs(CT9)])
	print(i)
	"""
	x=[CTAir,CT2,CT8,CT11,CT16,CT15,CT1,CT10,CT6,CT4,CT7,CT14,CT12,CT9]
	y=[0.002,0.28,0.40,0.942,0.977,1.0,1.018,1.053,1.097,1.143,1.154,1.335,1.56,1.825]
	plt.plot(x,y,marker="o",color="red",linestyle = "--")
	plt.show()
	"""
