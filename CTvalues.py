import numpy as np
import math
import matplotlib.pyplot as plt
import csv


def CTvalues():
	PI=math.pi
	r0=55
	r00=105
	r000=180

	x=np.empty(17)
	y=np.empty(17)

	theta0=(45/2+45*2)*PI/180
	x[0]=r00*math.cos(theta0)
	y[0]=r00*math.sin(theta0)

	theta1=(45/2+45*1)*PI/180
	x[1]=r00*math.cos(theta1)
	y[1]=r00*math.sin(theta1)

	theta2=(45/2+45*0)*PI/180
	x[2]=r00*math.cos(theta2)   
	y[2]=r00*math.sin(theta2)

	theta3=(45/2+45*(-1))*PI/180
	x[3]=r00*math.cos(theta3)
	y[3]=r00*math.sin(theta3)

	theta4=(45/2+45*(-2))*PI/180
	x[4]=r00*math.cos(theta4)
	y[4]=r00*math.sin(theta4)

	theta5=(45/2+45*(-3))*PI/180
	x[5]=r00*math.cos(theta5)
	y[5]=r00*math.sin(theta5)

	theta6=(45/2+45*(-4))*PI/180
	x[6]=r00*math.cos(theta6)
	y[6]=r00*math.sin(theta6)

	theta7=(45/2+45*(-5))*PI/180
	x[7]=r00*math.cos(theta7)
	y[7]=r00*math.sin(theta7)

	theta8=45*2*PI/180
	x[8]=r0*math.cos(theta8)
	y[8]=r0*math.sin(theta8)

	theta9=45*1*PI/180
	x[9]=r0*math.cos(theta9)
	y[9]=r0*math.sin(theta9)

	theta10=45*0*PI/180
	x[10]=r0*math.cos(theta10)
	y[10]=r0*math.sin(theta10)

	theta11=45*(-1)*PI/180
	x[11]=r0*math.cos(theta11)
	y[11]=r0*math.sin(theta11)

	theta12=45*(-2)*PI/180
	x[12]=r0*math.cos(theta12)
	y[12]=r0*math.sin(theta12)

	theta13=45*(-3)*PI/180
	x[13]=r0*math.cos(theta13)
	y[13]=r0*math.sin(theta13)

	theta14=45*(-4)*PI/180
	x[14]=r0*math.cos(theta14)
	y[14]=r0*math.sin(theta14)

	theta15=45*(-5)*PI/180
	x[15]=r0*math.cos(theta15)
	y[15]=r0*math.sin(theta15)

	#Air Angle=0
	x[16]=r000*math.sin(theta10)
	y[16]=r000*math.cos(theta10)


	#sum of mu for average
	sum=np.zeros(17)
        #sum of pixel for average
	count=np.zeros(17)
	
        for iy in range(height):
                Y =-iy+height/2-0.5
                for ix in range(width):
                        X=ix-width/2+0.5
                        d=(X-x)*(X-x)+(Y-y)*(Y-y)
			if d[0]<=25:
                                sum[0]+=f[ix+iy*width]
                                count[0]+=1
                        elif d[1]<=25:
                                sum[1]+=f[ix+iy*width]
                                count[1]+=1
                        elif d[2]<=25:
                                sum[2]+=f[ix+iy*width]
                                count[2]+=1
                        elif d[3]<=25:
                                sum[3]+=f[ix+iy*width]
                                count[3]+=1
                        elif d[4]<=25:
                                sum[4]+=f[ix+iy*width]
                                count[4]+=1
                        elif d[5]<=25:
                                sum[5]+=f[ix+iy*width]
                                count[5]+=1
                        elif d[6]<=25:
                                sum[6]+=f[ix+iy*width]
                                count[6]+=1
                        elif d[7]<=25:
                                sum[7]+=f[ix+iy*width]
                                count[7]+=1
                        elif d[8]<=25:
                                sum[8]+=f[ix+iy*width]
                                count[8]+=1
                        elif d[9]<=25:
                                sum[9]+=f[ix+iy*width]
                                count[9]+=1
                        elif d[10]<=25:
                                sum[10]+=f[ix+iy*width]
                                count[10]+=1
                        elif d[11]<=25:
                                sum[11]+=f[ix+iy*width]
                                count[11]+=1
                        elif d[12]<=25:
                                sum[12]+=f[ix+iy*width]
                                count[12]+=1
                        elif d[13]<=25:
                                sum[13]+=f[ix+iy*width]
                                count[13]+=1
                        elif d[14]<=25:
                                sum[14]+=f[ix+iy*width]
                                count[14]+=1
                        elif d[15]<=25:
                                sum[15]+=f[ix+iy*width]
                                count[15]+=1
                        elif d[16]<=25:
                                sum[16]+=f[ix+iy*width]
                                count[16]+=1
                                                                               
        #calculate average
	ave=sum/count
	
	CT=(ave-ave[14])/ave[14]*1000

	return CT[16],CT[1],CT[7],CT[10],CT[15],CT[14],CT[0],CT[9],CT[5],CT[3],CT[6],CT[13],CT[11],CT[8]

width=512
height=512

for i in range(1,2):
#for i in range(1,2):
	rawpath="/mnt/nfs_S65/Takayuki/package_TotalDensityEstimation/Recon/Recon7500/FBP_virtual_projection_512x512_gammex%d.raw" % i 
	fd=open(rawpath,'rb')
	f=np.fromfile(fd,dtype=np.float32,count=height*width)
	#img=f.reshape((height,width))
	CTvalues=CTvalues()
	fd.close()
	with open('CTvalues_abs.csv','a') as f:
		writer=csv.writer(f)
		#writer.writerow([CTAir,CT2,CT8,CT11,CT16,CT15,CT1,CT10,CT6,CT4,CT7,CT14,CT12,CT9])
		writer.writerow(CTvalues)
	print(i)
