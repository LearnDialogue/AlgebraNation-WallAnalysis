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

sql = "SELECT WP.`id`, comment_text FROM UsersBioInformation UBI inner join WallPosts WP ON UBI.useraccount_id = WP.useraccount_id;"   # LIMIT 1000

a.execute(sql)
doclist = []


f= open("mods.txt","w+")

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
		f.write("\n"+sentence)

except Exception as e:
	raise
	print(e)
else:
	pass
finally:
	pass

f.close() 
