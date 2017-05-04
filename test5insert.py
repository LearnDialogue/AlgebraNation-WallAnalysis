import pymysql
from nltk.corpus import stopwords

import MySQLdb

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()
val1 = 'hello1'
val2 = 'hello2'
try:
	
	sql = "INSERT INTO TopicTags (postGroup,threadwords) VALUES (%s,%s)"

	flag = a.execute(sql, (val1, val2))
	print flag
	conn.commit()
except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass


#print (a)
#print(data)