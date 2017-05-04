
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


doc = "A blood cell, also called a hematocyte, is a cell produced by hematopoiesis and normally found in blood."

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
print(lda_model.print_topic(max(lda_vector, key=lambda item: item[1])[0]))
