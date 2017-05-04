import pymysql
import nltk
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id , postGroup FROM PostUnlabelled;'

a.execute(sql)
threadwords = []
try:
	for row in a:
		
		stop = set(stopwords.words('english'))
		sentence = row[1]
		#print sentence
		sentenceWords = [i for i in sentence.lower().split() if i not in stop]
		for each in sentenceWords:
			threadwords.append(each)


except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

	conn.commit()

#print threadwords

all_words = nltk.FreqDist(threadwords)
print(all_words.most_common(50))