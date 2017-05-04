import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, subTopic, RawText FROM ConceptBag4;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		id = row[0]
		RawText = row[2]
		subTopic = row[1]
		conceptWords = [i for i in RawText.lower().split() if i not in stop]
		cwords = str(conceptWords)
		sql2 = "UPDATE ConceptBag4 SET conceptWords = %s where id ="+str(id)+";"
		flag = b.execute(sql2, cwords)
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