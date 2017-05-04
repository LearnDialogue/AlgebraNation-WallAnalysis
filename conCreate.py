import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT subTopic, RawText FROM ConceptBag;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
id = 1
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		RawText = row[1]
		subTopic = row[0]
		conceptWords = [i for i in RawText.lower().split() if i not in stop]
		cwords = str(conceptWords)
		sql2 = "UPDATE ConceptBag SET conceptWords = %s where id ="+str(id)+";"
		flag = b.execute(sql2, cwords)
		print flag
		id = id+1

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