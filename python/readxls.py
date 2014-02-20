from xlrd import open_workbook
import sys

###
###默认情况下，Python脚本文件是由utf-8编码，Python默认环境编码基本上是ascii编码方式，
###Python自然调用ascii编码解码程序去处理字符流，当字符流不属于ascii范围内，就会抛出异常（ordinal not in range(128)）
###解决方法是以下三行代码
###http://wangye.org/blog/archives/629/

reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

wb = open_workbook('qqi_android_key-en_20140219.xls')
for s in wb.sheets():
	print 'Sheet: ', s.name
	for row in range(s.nrows):
		values = []
		for col in range(s.ncols):
			#print str(s.cell(row,col).value)
			cell_value = s.cell(row,col).value
			values.append(str(s.cell(row, col).value))
			# if type(cell_value) != str:
			# 	#print cell_value
			# 	values.append(str(s.cell(row, col).value))
			# else:
			# 	values.append(s.cell(row, col).value)
		print row, values[0], '#', values[1]
	print


