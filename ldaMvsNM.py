
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

sql = 'SELECT id, postGroup, ManualTag FROM PostTagging_test1;'

a.execute(sql)


b = conn.cursor()
c = conn.cursor()
count = 0
totcount = 0
correctCount = 0

try:
	for row in a:
		
		doc = row[1]

		doc = doc.decode('utf-8', 'ignore')
		doc = doc.decode('windows-1252')
		doc = doc.replace('\n', ' ').replace('\r', '')
		#print sentence
		doc = doc.encode('utf-8', 'ignore')


		#print row[1]
		manualTag = row[2]
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
		#print(id2word_wiki)


		# doc = "A blood cell, also called a hematocyte, is a cell produced by hematopoiesis and normally found in blood."
		bow = id2word_wiki.doc2bow(tokenize(doc))
		#print(bow)


		# transform into LDA space
		lda_vector = lda_model[bow]
		#print(lda_vector)
		# print the document's single most prominent LDA topic
		#print(lda_model.print_topic(max(lda_vector, key=lambda item: item[1])[0]))
		
		mathLabels = ['0','1','5','9','12','13','16','17','22','23']
		#wordproblem mathlabels = 17
		# borderline cases = 7 , 19
		mathTags = ['APR','CED','REI','SSE','BF','IF','LE','NRN','ICQD','QU','PA','OM']

		tag = 'NM'
		for each in lda_vector:
			#print str(each[0])
			if str(each[0]) in mathLabels:
				#print each[0]
				tag = 'M'

		#print tag

		

		if manualTag in mathTags and tag=='M':
			evalp = "Y"
			correctCount+=1
		elif tag=='NM' and manualTag=='NM' :
			evalp="Y"
			correctCount+=1
		else:
			evalp = "N"

		sql2 = "UPDATE PostTagging_test1 SET ldaMathvsNM = %s where id ="+str(row[0])+";"
		flag = b.execute(sql2, (evalp))

		totcount+=1


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

print "Accuracy of Prediction is :"+ str(correctCount) +" / "+str(totcount)

#print (a)
#print(data)








