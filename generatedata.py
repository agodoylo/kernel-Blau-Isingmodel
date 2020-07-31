import _numpypy as np
import sys
from math import *

#read data:
#I have to read file by file all categories for the wards of interest. 
#voting:
fh=open('OriginalData/gla-elections-votes-all-2016_wards.csv','r')
#gla-elections-votes-all-2016.csv #london_wards_mine.csv
#https://data.london.gov.uk/dataset/london-elections-results-2016-wards-boroughs-constituency
igot=fh.readlines()
del igot[0]
del igot[0]
del igot[0]
del igot[0]
fh.close()

lasta='Bexley'
area=0
ward=0
darea={}
dward={}

fh4=open('OriginalData/2011censuswardscoord.csv','r') #wardscoord.dat
#from UK2011Censuswards.csv with wards polygons should I repeated withgeopandas? at least I can check if they are correct or post the good numbers.
#https://www.statistics.digitalresources.jisc.ac.uk/dataset/2011-census-geography-boundaries-wards-and-electoral-divisions
#infuse_ward_lyr_2011.shp from a new program wardscentroidpandas.py 2011censuswardscoordpandas.csv
igot4=fh4.readlines()
centro={}
for line in igot4:
	about = line.strip().split(',')
	centro[about[0]]=[about[1],about[2]]
fh4.close()
#fout=open('LondonMayorfiltered_more.dat','w')
#fouta=open('LondareaID_more.dat','w')
#foutw=open('LondwardID_more.dat','w')
darea[lasta]=area	
#fouta.write('%s %s\n' % (lasta,area))

moredw={}
moredw['E05009367']='E05000231'
moredw['E05009368']='E05000232'
moredw['E05009369']='E05000234'
moredw['E05009370']='E05000235'
moredw['E05009371']='E05000236'
moredw['E05009372']='E05000237'
moredw['E05009373']='E05000238'
moredw['E05009374']='E05000239'
moredw['E05009378']='E05000241'
moredw['E05009379']='E05000242'
moredw['E05009382']='E05000246'
moredw['E05009385']='E05000248'
moredw['E05009317']='E05000573'
moredw['E05009318']='E05000575'
moredw['E05009319']='E05000576'
moredw['E05009320']='E05000577'
moredw['E05009326']='E05000580'
moredw['E05009332']='E05000586'
moredw['E05009333']='E05000587'
moredw['E05009329']='E05000584'
moredw['E05009330']='E05000585'
moredw['E05009334']='E05000584'
moredw['E05009335']='E05000588'
moredw['E05009336']='E05000589'
moredw['E05009388']='E05000382'
moredw['E05009389']='E05000383'
moredw['E05009390']='E05000384'
moredw['E05009392']='E05000385'
moredw['E05009393']='E05000386'
moredw['E05009395']='E05000388'
moredw['E05009396']='E05000389'
moredw['E05009397']='E05000391'
moredw['E05009398']='E05000392'
moredw['E05009399']='E05000393'
moredw['E05009400']='E05000394'
moredw['E05009401']='E05000395'
moredw['E05009402']='E05000396'
moredw['E05009403']='E05000397'
moredw['E05009405']='E05000399'
defdic={}
forget=0.
more=0
for line in igot:
	about = line.strip().split(',')
	#if len(about)!=8:
	#	print 'about'
	#try:
	print about
	saq=float(about[11])
	cons=float(about[12])
	re=float(about[11])/(saq+cons)
	if about[0]!=lasta:
		lasta=about[0]
		area=area+1	
		darea[about[0]]=area	
		#fouta.write('%s %s\n' % (about[0],area))
	#fout.write('%s %s %s %s %s %s\n' % (area,ward,re,saq+cons, float(about[23]),(float(about[23])-(saq+cons))/float(about[23]) ))
	#area: area ID; ward: ward ID; re: frac of labor, labor/(lab+cons); saq+cons
	forget=forget+(float(about[23])-(saq+cons))/float(about[23])
	if area in [7,9,24,31]:
		try:
			defdic[moredw[about[4]]]=[area,re]
			#[area,ward,re,saq+cons]
			dward[moredw[about[4]]]=ward
			#foutw.write('%s %s %s\n' % (moredw[about[4]],ward,area))
			more=more+1
			#print 'yes', about[4],moredw[about[4]]
		except KeyError:
			defdic[about[4]]=[area,re]
			dward[about[4]]=ward
			#foutw.write('%s %s %s\n' % (about[4],ward,area))
	else:
		defdic[about[4]]=[area,re]
		dward[about[4]]=ward
		#foutw.write('%s %s %s\n' % (about[4],ward,area))
	ward=ward+1
	#except ValueError:
	#	print 'errrrrrrrrrrrrr',line
	#	pass
#fout.close()
#fouta.close()
#foutw.close()

#2012 Elections:
fh2=open('OriginalData/Lower_Layer_Super_Output_Area__2001__to_Ward__2010__Lookup_in_England_and_Wales.csv','r')
#Lower_Layer_Super_Output_Area__2001__to_Ward__2010__Lookup_in_England_and_Wales.csv 
#https://geoportal.statistics.gov.uk/datasets/lower-layer-super-output-area-2001-to-ward-2010-lookup-in-england-and-wales/data
igot2=fh2.readlines()
del igot2[0]
trans={}
for line in igot2:
	about = line.strip().split(',')
	trans[about[3]]=about[2]
fh2.close()
#E01000001,City of London 001A,E05000001,00AAFA,Aldersgate
#I need re and saq+cons from May2012:

fh2=open('OriginalData/gla-elections-votes-ward-2012_wards.csv','r')
#gla-elections-votes-ward-2012.csv
#https://data.london.gov.uk/dataset/london-elections-results-2012-wards-boroughs-constituency
igot2=fh2.readlines()
print len(igot2)
del igot2[:11]
print len(igot2)
print igot2[0]

res12={}

for line in igot2:
	about = line.strip().split(',')
	#if len(about)!=8:
	#	print 'about'
	#try:
	#print about
	saq=float(about[13])
	cons=float(about[11])
	re=saq/(saq+cons)
	try:
		#res12[trans[about[0]]]=re
		defdic[trans[about[0]]].append(re)
	except KeyError:
		#print about[0]
		pass
fh2.close()


print 'total average forguet', forget/float(ward)

#income:
fh2=open('OriginalData/ward-profiles-excel-version.csv','r')
#ward-profiles-excel-version\ \(1\).csv float 32 (es el elemento 33)
#https://data.london.gov.uk/dataset/ward-profiles-and-atlas
igot2=fh2.readlines()
del igot2[0]

inc={}

for line in igot2:
	about = line.strip().split(',')
	inc[about[2]]=float(about[32])/1000.

fh2.close()

#Varaibles:
#Education: 11elements ward code (2), 5 categories (no missing) 0:noqualification 1 level1 ...4 level4
fh=open('OriginalData/2017121816246549_AGE_HIQUAL_UNIT/Data_AGE_HIQUAL_UNIT.csv','r')
igot=fh.readlines()
del igot[0]
fh.close()

tot=0
nw=0
for line in igot:
	about = line.strip().split(',')
	#print about[1]
	if about[1] in defdic.keys():
		loc=[]
		data=[]
		for i in range(5):
			n=int(about[len(about)-(6-i)])
			data=data+[i]*n
			tot=tot+n
			loc.append(float(about[len(about)-(6-i)]))
		nw=nw+1
		sis=sum(loc)
		#print 'sis',sis,len(data)
		amed=0.
		for i in range(5):
			amed=amed+i*loc[i]/float(sis)
		defdic[about[1]].append(amed)
		#print vec, sum(vec)
print 'tot wards EQ',tot	
		

fh=open('OriginalData/1b12018115151351415_AGE_UNIT/Data_AGE_UNIT.csv','r')
igot=fh.readlines()
igori=igot[1]
oriab = igori.strip().split(',')
age=[]
for i in range(87):
	try:
		a=oriab[len(oriab)-(88-i)]
		b=float(a.replace('Age : Age ','').replace(' - Unit : Persons',''))
		age.append(b)
	except ValueError:
		print a.replace('Age : Age ','').replace(' - Unit : Persons','')
		age.append(100.)
del igot[0]
del igot[1]
fh.close()

tot=0
nw=0
for line in igot:
	about = line.strip().split(',')
	#print about[1]
	if about[1] in defdic.keys():
		#print 'helooooooooooooooo', line
		data=[]
		sis=0.
		amed=0.
		for i in range(87):
			if age[i]>18:
				n=int(float(about[len(about)-(88-i)]))
				sis=sis+n
				amed=amed+age[i]*n
				data=data+[age[i]]*n
				tot=tot+n
		nw=nw+1
		amed=amed/float(sis)
		defdic[about[1]].append(amed)

fh=open('OriginalData/201812131062425_AGE_SEX_UNIT/Data_AGE_SEX_UNIT.csv','r')
igot=fh.readlines()
igori=igot[1]
oriab = igori.strip().split(',')
gen=[]
gen2=[]
for i in range(40):
		aa=oriab[len(oriab)-(41-i)]
		gen2.append(aa)
		a=aa.strip().split(' ')
		gen.append(a.count('Females'))
	
print gen
print gen2
fh.close()

tot=0
nw=0
size=[]
for line in igot:
	about = line.strip().split(',')
	#print about[1]
	if about[1] in defdic.keys():
		data=[]
		sis=0.
		amed=0.
		for i in range(40):
			n=int(about[len(about)-(41-i)])
			sis=sis+n
			amed=amed+gen[i]*n
			data=data+[gen[i]]*n
			tot=tot+n
		nw=nw+1
		amed=amed/float(sis)
		#print 'sex', amed
		defdic[about[1]].append(amed)
		defdic[about[1]].append(centro[about[1]][0])
		defdic[about[1]].append(centro[about[1]][1])
		defdic[about[1]].append(inc[about[1]])
		defdic[about[1]].append(sis) #size according to census data

#write de data file:
#fout=open('LondonMayor-coordcentroids_more.dat','w')
fout=open('ME16-12_sociodemographics.dat','w')
#fout.write('area,ward,re,saq+cons,edu,age,gender, lon lat,size \n')
fout.write('0ward 1area 2may16 3may12 4edu 5age 6gender 7xcoord 8ycoord 9income(£1000) 10size\n')
for e in defdic.keys():
	if len(defdic[e])>5:
		fout.write('%s ' % e)
		for i in range(len(defdic[e])):
			fout.write('%s ' % defdic[e][i])
		fout.write('\n')
fout.close()
print 'moreeeeeeeeeeeeeeeee', more

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EU Referendum data and Borough data

fh=open('OriginalData/ward-results.csv','r')
#ward-results.xlsx
#https://3859gp38qzh51h504x6gvv0o-wpengine.netdna-ssl.com/files/2017/02/ward-results.xlsx
fout=open('EUwards.dat','w')
igot=fh.readlines()
for line in igot:
	about = line.strip().split(',')
	if about[0] in defdic.keys():
		try:
			a=float(about[6])/100.
			fout.write('%s %s\n' % (about[0],a))
		except ValueError:
			pass
fh.close()
fout.close()

GLBoroughs=['E09000002','E09000003','E09000004','E09000005','E09000006','E09000007','E09000008','E09000009','E09000010',
'E09000011','E09000012','E09000013','E09000014','E09000015','E09000016','E09000017','E09000018','E09000019','E09000020',
'E09000021','E09000022','E09000023','E09000024','E09000025','E09000026','E09000027','E09000028','E09000029','E09000030',
'E09000031','E09000032','E09000033']
Bou={}
#Bre, may16, may12, may08, may04
#https://data.london.gov.uk/dataset/eu-referendum-results EU-referendum-result-data.csv (remove ,)
fh=open('OriginalData/EU-referendum-result-data.csv','r')
igot=fh.readlines()
del igot[0]
for line in igot:
	about = line.strip().split(',')
	if about[3] in GLBoroughs:
		Bou[about[3]]=[float(about[11])/(float(about[11])+float(about[12]))]
fh.close()

fh=open('OriginalData/gla-elections-2000-2016.csv','r')
#Borough level all together: https://data.london.gov.uk/dataset/london-elections-results-2016-wards-boroughs-constituency
#gla-elections-2000-2016.csv
igot=fh.readlines()
del igot[0]
ands={}
for line in igot:
	about = line.strip().split(',')
	if about[0] in GLBoroughs:
		Bou[about[0]].append(float(about[21])/(float(about[21])+float(about[17]))) #2016
		Bou[about[0]].append(float(about[20])/(float(about[20])+float(about[16]))) #2016
		ands[about[0]]=about[1]
		if about[1]=='Barking and Dagenham':
			ands[about[0]]='Barking & Dagenham'
		if about[1]=='Hammersmith and Fulham':
			ands[about[0]]='Hammersmith & Fulham'
		if about[1]=='Kensington and Chelsea':
			ands[about[0]]='Kensington & Chelsea'
print darea
fout=open('ME16-12EUBoroughs.dat','w')
fout.write('ID,Code,EUreferendum,ME2016,ME2012\n')
for e in Bou.keys():
	fout.write('%s %s %s %s %s\n' % (darea[ands[e]],e,Bou[e][0],Bou[e][1],Bou[e][2]))
fout.close()	


		



