import pymysql
from nltk.corpus import stopwords


import sys
reload(sys)
sys.setdefaultencoding('utf-8')



import time
ts = time.time()
print ts

import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st



conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()

sql = 'SELECT id, postGroup FROM PostUnlabelled;'   # LIMIT 1000

a.execute(sql)
doclist = []




try:
	for row in a:
		
		sentence = row[1]
		
		#print sentence
		#sentence = sentence.encode('ascii', 'ignore')
		#sentence = unicode(sentence, 'utf-8')
		sentence = sentence.decode('utf-8', 'ignore')
		sentence = sentence.decode('windows-1252')
		sentence = sentence.replace('\n', ' ').replace('\r', '')
		#print sentence
		sentence = sentence.encode('utf-8', 'ignore')
		doclist.append(sentence)

except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

print row[0]
#print doclist


doc_complete = doclist

from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
import string


# Importing Gensim
import gensim
from gensim import corpora



stop = set(stopwords.words('english'))
#exclude = set(string.punctuation) 
#lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    #punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    #normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return stop_free

doc_clean = [clean(doc).split() for doc in doc_complete]  
#print doc_clean


# Creating the term dictionary of our courpus, where every unique term is assigned an index. 
dictionary = corpora.Dictionary(doc_clean)

# ignore words that appear in less than 2 documents or more than 10% documents
dictionary.filter_extremes(no_below=3)
#print(id2word_wiki)

print 'doc2bow started'
# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

#print doc_term_matrix

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

LdaMulti = gensim.models.ldamulticore.LdaMulticore

print 'lda training started'

# Running and Trainign LDA model on the document term matrix.
ldamodel = LdaMulti(doc_term_matrix, num_topics=25, id2word = dictionary, passes=15)

ldamodel.save('ldamodel1.model')

print(ldamodel.print_topics(num_topics=25, num_words=20))



import time
ts2 = time.time()
timetaken= ts2-ts

import datetime
st = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
print st

print '\n\nTime taken to run: '
st = datetime.datetime.fromtimestamp(timetaken).strftime('%Y-%m-%d %H:%M:%S')
print st







