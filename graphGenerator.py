import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import pandas
from numpy import genfromtxt

# enter name of the simulation here:
name ='new2(20171217_1558)/new2(20180115_1623)'

for i in range(0, 1500, 24):
	# filetoread ='D:/Bio research/Work space/Cdynomics_Amitesh/resultss/'+ name +'/SpacialDistributionDeadCellsData/agent_State('+str(i)+').csv'
	filetoread ='D:/Bio research/Work space/Cdynomics_Amitesh/resultss/'+ name +'/SpacialDistributionData/agent_State('+str(i)+').csv'
	# output = 'D:/Bio research/Work space/Cdynomics_Amitesh/resultss/'+ name +'/SpacialDistributionData_Oleate/agent_State_Oleate('+str(i)+').png'
	output = 'D:/Bio research/Work space/Cdynomics_Amitesh/resultss/'+ name +'/SpacialDistributionData/agent_State('+str(i)+').png'
	print filetoread
	df = pandas.read_csv(filetoread)
	fig = plt.figure()
	labels = ['0','1','180','270','360','450','630+']
	# labels = []
	y=df['radius']
	x1=df['Clostridium1']
	t1=plt.plot(x1,'green',label='Clostridium1',linewidth=2)
	x2=df['Clostridium2']
	t2=plt.plot(x2,'red',label='Clostridium2',linewidth=2)
	x3=df['Methanogen1']
	t3=plt.plot(x3,'blue',label='Methanogen1',linewidth=2)
	x4=df['Methanogen2']
	t4=plt.plot(x4,'cyan',label='Methanogen2',linewidth=2)
	x5=df['Desulfovibrio']
	t5=plt.plot(x5,'yellow',label='Desulfovibrio',linewidth=2)
	# x6=df['Desulfovibrio2']
	# t6=plt.plot(x6,'magenta',label='Desulfovibrio2',linewidth=2)
	x7=df['OleateDegrader']
	t7=plt.plot(x7,'red',label='OleateDegrader',linewidth=2)
	x8=df['Dead cells']
	t8=plt.plot(x8,'black',label='Died cells',linewidth=2)
	ax=plt.axes()
	plt.xlabel('Radius(mkm)')
	plt.ylabel('Number of cells')
	plt.legend(loc='upper center', bbox_to_anchor=(0.6, 1.08),
          ncol=3, fancybox=True, shadow=True, fontsize = 'small')
	plt.title('Hour: '+ str(i), loc='left')
	# labels = [item.get_text() for item in ax.get_xticklabels()]
	# labels[0]='0'
	labels[0]='0-90'
	labels[1]='90-180'
	labels[2]='180-270'
	labels[3]='270-360'
	labels[4]='360-450'
	labels[5]='450-540'
	labels[6]='540-630+'
	# labels[6]='630+'
	# print ax.get_xticklabels()
	ax.set_xticklabels(labels)
	ax.set_ylim([0, 40000])
	
	# ax.grid()
	# plt.show()
	plt.show(block=False)
	plt.savefig(output)
	# plt.close()
