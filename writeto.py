import xlwt
import xlrd
import xlsxwriter
  
workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0

f = open('C:/Users/DELL/out1.txt', 'r+')

data = f.readlines() # read all lines at once
for i in range(len(data)):
 # write operation perform
    worksheet.write(row, column, data[i])
    row += 1

workbook.close()
f.close()