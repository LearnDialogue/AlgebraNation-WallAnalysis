import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, postGroup FROM PostTagging_test1;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
c = conn.cursor()

try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		threadText = row[1]
		threadtokens = [i for i in threadText.lower().split() if i not in stop]
		sql2 = "Select * from ConceptBag2"
		tag = "NM"
		matchcount = 0
		matchStore = []
		b.execute(sql2)
		for conceptrow in b:
			ConceptBagRaw = conceptrow[2]
			concepttokens = [i for i in ConceptBagRaw.lower().split() if i not in stop]
			matches = list(set(threadtokens).intersection(set(concepttokens)))
			if len(matches)>matchcount:
				matchcount = len(matches)
				tag = conceptrow[5]
				matchStore = matches

		matchWords = str(matchStore)
		sql2 = "UPDATE PostTagging_test1 SET matchedConceptWords = %s, predictedTag = %s where id ="+str(row[0])+";"
		flag = c.execute(sql2, (matchWords, tag))
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