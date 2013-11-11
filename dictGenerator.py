
#make dictionaries of all the words in paper.txt
from collections import Counter
counter = Counter()
with open('paper.txt', 'r') as file:
    for line in file:
    	newline=line.split(';')[1]
    	for word in newline.split():
    		counter[word] += 1

#dump all the words sequentially into vocab.txt.One word per
vocabDict= Counter()
iterator=0
with open('vocab.txt', 'r') as file:
	for line in file:
		line=line.rstrip()
		vocabDict[line]=iterator
		iterator=iterator+1

#generate title.txt from paper.txt
#uses the vocab dict to figure out the numbers corresponding to each word in the title
f1=open('title.txt', 'w+')
with open('paper.txt', 'r') as file:
    for line in file:
    	titleCounter=Counter()
    	paperID=line.split(';')[0]
    	a=paperID+" "
    	paperTitle=line.split(';')[1]
	for word in paperTitle.split():
		titleCounter[word]+=1
	f1.write(str(len(titleCounter))+" ")
        for key in titleCounter:
		print key
		print vocabDict[key]
		f1.write(str(vocabDict[key])+":"+str(titleCounter[key])+" ")
	f1.write("\n")
