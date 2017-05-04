import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, primaryTopic FROM tagged_posts LIMIT 1000;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
c = conn.cursor()
count = 0
try:
	for row in a:
		
		tag = row[1]
		print row[0]
		x = 0
		sql2 = "UPDATE PostTagging_test1 SET predictedTag = "+'0'+", ManualTag= %s where id ="+str(row[0])+";"
		flag = c.execute(sql2, (tag))
		count = count + flag

except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

	conn.commit()

print count

#print (a)
#print(data)