
import gensim
from gensim import corpora, models, similarities

from nltk.corpus import stopwords 


lda_model =  models.LdaModel.load('ldamodel1.model')

# print all topics
#print model.show_topics()

#print(model.print_topics(num_topics=25, num_words=20))



#doc_lda = lda[doc_bow]

from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import smart_open, simple_preprocess

def tokenize(text):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]




import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, postGroup, ManualTag FROM PostTagging_test1 LIMIT 10;'

a.execute(sql)

#countrow = a.execute(sql)

#print ("Number of rows :",countrow)
#data = a.fetchall()

x = '''0 NM  Call for help.
		1 Math
		2 Math
		3 NM  moderation
		4 NM  names  moderation.
		5 Math
		6 NM  socialize  locations, dates, cost, numbers. could be math as well
		7 Math - geometry - could be NM
		8 NM - socialize
		9 Math - equations and numbers.
		10 NM
		11 NM - karma points - welcome
		12 Math
		13 Math
		14 NM - karma points
		15 NM - reference to sections and videos
		16 Math
		17 Math - Geometry
		18 NM
		19 Math -
		20 NM - questioning, looking for answers.
		21 NM - Moderation
		22 Math - Word problems
		23 Math - profit loss
		24 NM - Greetings - good byes and thank you'''

mathLabels = ['0','1','5','7','9','12','13','16','17','19','22','23']

b = conn.cursor()
c = conn.cursor()
count = 0
try:
	for row in a:
		
		doc = row[1]
		print row[1]
		stop = set(stopwords.words('english'))
		#exclude = set(string.punctuation) 
		#lemma = WordNetLemmatizer()
		def clean(doc):
		    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
		    #punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
		    #normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
		    return stop_free

		doc_clean = [clean(doc).split()]  


		id2word_wiki = gensim.corpora.Dictionary(doc_clean)
		print(id2word_wiki)


		# doc = "A blood cell, also called a hematocyte, is a cell produced by hematopoiesis and normally found in blood."
		bow = id2word_wiki.doc2bow(tokenize(doc))
		print(bow)


		# transform into LDA space
		lda_vector = lda_model[bow]
		print(lda_vector)
		# print the document's single most prominent LDA topic
		#print(lda_model.print_topic(max(lda_vector, key=lambda item: item[1])[0]))
		tag = ''
		for each in lda_vector:
			if each[0] in mathLabels:
				tag = 'M'
			else:
				tag = 'NM'

		print tag






		x = '''0 NM  Call for help.
		1 Math
		2 Math
		3 NM  moderation
		4 NM  names  moderation.
		5 Math
		6 NM  socialize  locations, dates, cost, numbers. could be math as well
		7 Math - geometry - could be NM
		8 NM - socialize
		9 Math - equations and numbers.
		10 NM
		11 NM - karma points - welcome
		12 Math
		13 Math
		14 NM - karma points
		15 NM - reference to sections and videos
		16 Math
		17 Math - Geometry
		18 NM
		19 Math -
		20 NM - questioning, looking for answers.
		21 NM - Moderation
		22 Math - Word problems
		23 Math - profit loss
		24 NM - Greetings - good byes and thank you'''

		#print x

		print "-------------------------"
		print "-------------------------"



		# x = 0
		# sql2 = "UPDATE PostTagging_test1 SET predictedTag = "+'0'+", ManualTag= %s where id ="+str(row[0])+";"
		# flag = c.execute(sql2, (tag))
		# count = count + flag

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








