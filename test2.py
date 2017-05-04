import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT comment_text FROM WallPosts LIMIT 100;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		sentence = row[0]
		print [i for i in sentence.lower().split() if i not in stop]
#['foo', 'bar', 'sentence']




except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass


#print (a)
#print(data)