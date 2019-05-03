from xlrd import open_workbook, XLRDError
import sys



class XlsToIni :
	def toIni(self, xlsFile, iniFile):
		x =  open_workbook(xlsFile)
		sheet=x.sheet_by_name('ConfigList') 

		
		f=open(iniFile,"w+")

		
		a_status=""
                                     
		for i in range(3,(sheet.nrows)):
			for j in range(2,(sheet.ncols)):
				val=str(sheet.cell_value(i,j))
				if('GROUP' in val):
					f.write("\n["+val+"]\n")
				elif(j==2 and val!=''):
				    	a_status=val
					f.write("["+val+"]\n")
				elif(j==3 and val!=''):
					f.write("name = \""+val+"\"\n")
				elif(j==4 and val!=''):
					f.write("rvalue = "+val+"\n")
				elif(j==5 and val!=''):
					f.write("type = "+val+"\n")
				elif(j==6 and val!=''):
				   	 if('A' in a_status):
						val=val.split('-')
						f.write("rmin = "+val[0]+"\n")
					
						f.write("rmax = "+val[1]+"\n")
				     		f.write("unit = "+val[2]+"\n")
				     	 else:
						f.write("rmin, rmax, unit = "+val+"\n")
				elif(j==7 and val!=''):
					if(('Yes' in val) or ('yes' in val)):
						f.write("favr = 1\n")
					if(('No' in val) or ('no' in val)):
						f.write("favr = 0\n")
				elif(j==8 and val!=''):
					if(('Yes' in val) or ('yes' in val)):
						f.write("writ = 1\n")
					if(('No' in val) or ('no' in val)):
						f.write("writ = 0\n")
				elif(j==9 and val!=''):
					f.write("dval = "+val+"\n")
				elif(j==10 and val!=''):
					f.write("desc = \""+val+"\"\n")
				else:
					if(val):
						f.write(val+"\n")
			f.write("\n")
		
xlsFile = sys.argv[1]
iniFile = sys.argv[2]

XlsToIni().toIni(xlsFile, iniFile)
