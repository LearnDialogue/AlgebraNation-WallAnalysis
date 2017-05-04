import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT postGroup FROM PostTagging LIMIT 10;'

a.execute(sql)
doclist = []
try:
	for row in a:
		
		sentence = row[0]
		doclist.append(sentence)

except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

print doclist


#print (a)
#print(data)