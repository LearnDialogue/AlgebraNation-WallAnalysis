import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id , comment_text FROM WallPosts where is_parent_post=1 order by `ts_created`;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
c = conn.cursor()
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		sentence = row[1]
		#print [i for i in sentence.lower().split() if i not in stop]
		
		mainid = row[0]
		sql2 = 'SELECT comment_text FROM WallPosts where reply_to_post_id='+str(mainid)+';'
		b.execute(sql2)
		for comment in b:
		
			sentence = sentence + '\n' +comment[0]
		
		sentence = sentence.replace('"','')
		threadwords = [i for i in sentence.lower().split() if i not in stop]
		#sqlInsert = 'INSERT INTO TopicTags (postGroup,threadwords) VALUES ('+sentence+','+str(threadwords)+')'
		tw = str(threadwords)
		if mainid%40 == 0:
			sqlInsert2 = "INSERT INTO PostTagging (postParentID, postGroup,threadwords) VALUES (%s, %s,%s)"
		else:
			sqlInsert2 = "INSERT INTO PostUnlabelled (postParentID, postGroup,threadwords) VALUES (%s,%s,%s)"

		c.execute(sqlInsert2, (mainid,sentence, tw))
		#print flag
		#print tw

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