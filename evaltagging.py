import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, predictedTag, ManualTag FROM PostTagging_test1;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()

totcount = 0
correctCount = 0

try:
	for row in a:
		
		predictedTag = row[1]
		ManualTag = row[2]
		if predictedTag==ManualTag:
			evalp = "Y"
			correctCount+=1
		else:
			evalp = "N"

		sql2 = "UPDATE PostTagging_test1 SET PredCorrect = %s where id ="+str(row[0])+";"
		flag = b.execute(sql2, (evalp))
		print flag

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