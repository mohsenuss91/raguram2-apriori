from collections import Counter
vocabDict= {}
iterator=0
with open('vocab.txt', 'r') as file:
	for line in file:
		line=line.rstrip()
		vocabDict[line]=iterator
		iterator=iterator+1
#print vocabDict

with open('word_assignment_stripped.dat', 'r') as file:
    for line in file:
    	words=line.split()
	topicDict={}
	for word in words:
		tup=word.split(':')
		try:
			topicDict[tup[1]].append(tup[0])
		except KeyError:
			topicDict[tup[1]] = [tup[0]]

	for key in topicDict:
		filename="topic-"+str(int(key))+".txt"
		fp=open(filename,'a+b')
		fp.write(" ".join(topicDict[key])+"\n")
				
			
			
	
		
