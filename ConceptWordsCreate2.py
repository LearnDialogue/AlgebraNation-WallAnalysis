import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT acronym, RawText FROM ConceptBag4;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		RawText = row[1]
		acr = row[0]
		print RawText
		conceptWords = [i for i in RawText.lower().split() if i not in stop]
		print conceptWords
		print acr
		sql2 = "UPDATE ConceptBag4 SET conceptWords = %s where acronym = %s";
		flag = b.execute(sql2, (conceptWords, acr))
		print flag

except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

	conn.commit()


#print (a)
#print(data)