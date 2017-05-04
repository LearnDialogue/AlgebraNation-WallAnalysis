
from goose import Goose
import json

import requests
import urllib

import pymysql
from nltk.corpus import stopwords

conn=pymysql.connect(host='127.0.0.1',user='root', passwd='root',port=8889,db='AlgebraNationWall')
a = conn.cursor()




#Offline populating the db with concepts from file
	
concepts = [line.rstrip('\n') for line in open('concepts/APR')]
print concepts
for i in concepts:	

	# devKey = 'AIzaSyA7Nzbmsfwuz7D9rtq1s8la-2Y1LsOVfe4'
	# query = 'cognitive science'
	# cx = '001737285016961477263%3Afr_yrjtwv_8'
	con = i
	query = i.replace (" ", "+")
	#payload = {'q': query, 'cx': cx, 'key' : devKey}
	# r = requests.get('https://www.googleapis.com/customsearch/v1', params=payload)
	# print r.url
	# print r.text

	f = urllib.urlopen("https://www.googleapis.com/customsearch/v1?q="+query+"&cx=001737285016961477263%3Afr_yrjtwv_8&key=AIzaSyA7Nzbmsfwuz7D9rtq1s8la-2Y1LsOVfe4")
	r =  f.read()
	searchResponse = json.loads(r)	

	print searchResponse

	for searchResult in searchResponse['items']:
		title = searchResult['title']
		link = searchResult['link']

		excludelist = ['coursera', 'edx', 'pdf', 'youtube.com', 'ocw.mit.edu','amazon','flipkart','onlinelibrary.wiley.com',
							'udacity','udemy']
		flag = 0
		for i in excludelist:
			if i in link:
				print 'Found exclusion : '+link
				flag = 1
		if flag == 0 :
			# if(Link.objects.filter(url=link).exists()):
			# 	print 'exists : '+link
			# else:
				g = Goose()
				
				print link
				try:
					artic = g.extract(url=link)
					article = artic.cleaned_text.encode("utf-8")
					title = artic.title.encode("utf-8")
					wordCount=len(article.split())

					topic = 'Algebra'
					subTopic = 'APR'
					try:
						
						sql = "INSERT INTO AlgebraDataset2 (Topic,subTopic,concept,url,title,document) VALUES (%s,%s,%s,%s,%s,%s)"

						flag = a.execute(sql, (topic, subTopic, con,link,title,article))
						print flag
						conn.commit()
					except Exception as e:
						raise
						print(e)
					else:
						pass
					finally:
						pass


					print 'Inserted data for '+link
				except (RuntimeError, TypeError, NameError) as e:
					print 'exception occured with : '+link
					print 'The error is : '+str(e)
					pass