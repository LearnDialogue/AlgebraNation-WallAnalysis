import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, predictedTags, ManualTag FROM PostTagging_test3;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()

totcount = 0
correctCount = 0

mathTags = ['APR','CED','REI','SSE','BF','IF','LE','NRN','ICQD','QU','PA','OM','PAAPR','PACED','PAREI','PASSE','PABF','PAIF','PALE','PANRN','PAICQD','PAQU','PA','PAOM']

try:
	for row in a:
		
		predictedTags = row[1]
		ManualTag = row[2]
		#predictedTag=="NM" && ManualTag=="NM":
		predictedTagsExtract = predictedTags.split("'")[1::2];
		for predictedTag in predictedTagsExtract:
			#print predictedTag
			if predictedTag in mathTags and ManualTag in mathTags:
				evalp = "Y"
				correctCount+=1
				break
			elif predictedTag=='NM' and ManualTag=='NM' :
				evalp="Y"
				correctCount+=1
				break
			else:
				evalp = "N"

		sql2 = "UPDATE PostTagging_test3 SET BaseMathvsNM = %s where id ="+str(row[0])+";"
		flag = b.execute(sql2, (evalp))

		totcount+=1

except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

	conn.commit()

	print "Accuracy of Prediction is :"+ str(correctCount) +" / "+str(totcount)


#print (a)
#print(data)