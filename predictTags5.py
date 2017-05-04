import pymysql
from nltk.corpus import stopwords
import operator

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, postGroup FROM PostTagging_test3;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

b = conn.cursor()
c = conn.cursor()

totcount = 0
correctCount = 0

try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		threadText = row[1]
		threadtokens = [i for i in threadText.lower().split() if i not in stop]
		sql2 = "Select * from ConceptBag4"
		tag = "NM"
		matchcount = 0
		matchStore = {}
		matchedTags = {}
		b.execute(sql2)
		for conceptrow in b:
			ConceptBagRaw = conceptrow[2]
			concepttokens = [i for i in ConceptBagRaw.lower().split() if i not in stop]
			matches = list(set(threadtokens).intersection(set(concepttokens)))
			if len(matches)>0:
				matchcount = len(matches)
				tag = conceptrow[5]
				matchedTags[tag] = matchcount
				#append to the bigger list of <tag,matches> 
				matchStore[tag] = matches
		if len(matchStore)==0:
			matchedTags[tag]=1

		matchWords = str(matchStore)

		# sort the matchedTags by value
		#print matchedTags
		sorted_tags = sorted(matchedTags.items(), key=operator.itemgetter(1),reverse=True)

		#fetch all the tags
		#loop over all the (top 2/3/4/5) tags and see if they match with ManualTag
		evalp = "N"

		for key, value in sorted_tags.iteritems():
			#put a check on value
			if key == ManualTag:
				evalp = "Y"
				correctCount+=1
				break

		sql2 = "UPDATE PostTagging_test4 SET PredCorrect = %s where id ="+str(row[0])+";"
		flag = b.execute(sql2, (evalp))
		#print flag
		totcount+=1



		sorted_tags= str(sorted_tags)
		#print sorted_tags
		sql2 = "UPDATE PostTagging_test3 SET matchedConceptWords = %s, predictedTags = %s where id ="+str(row[0])+";"
		flag = c.execute(sql2, (matchWords, sorted_tags))
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