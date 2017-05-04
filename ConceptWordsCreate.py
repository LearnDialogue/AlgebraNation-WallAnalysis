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
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		RawText = row[1]
		subTopic = row[0]
		conceptWords = [i for i in RawText.lower().split() if i not in stop]

		sql2 = "UPDATE ConceptBag SET conceptWords = %s where subTopic = %s";
		flag = b.execute(sql2, (conceptWords, subTopic))
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