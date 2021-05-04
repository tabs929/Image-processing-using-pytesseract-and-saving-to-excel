import re
import xlwt
import xlrd
import xlsxwriter

txt=open("C:/Users/DELL/out_text.txt")

db=txt.read()
res=re.findall('(Ingredients)(?s)(.*?)(Instructions)',db)

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0


#outfile = "out2.xlxs"
#f = open(outfile, "a")

for result in res:
    #f.write(' '.join(str(s) for s in result) + '\n')
    worksheet.write(row, column, ' '.join(str(s) for s in result) + '\n')
    row += 1


##print(second.group(0))
#text=second.group(0)


 
#text = text.replace('-\n', '')      
#f.write(text)
  
# Close the file after writing all the text.
#txt.close()

workbook.close()
txt.close()