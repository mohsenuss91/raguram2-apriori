vocabDict= {}
it=0
with open('vocab.txt', 'r') as file:
    for line in file:
        line=line.rstrip()
        vocabDict[int(it)]=line
        it=it+1

for i in range(5):
    filename="pattern-"+str(i)+".txt"
    outputPath1="./pattern/"+filename
    outputPath2="./pattern/pattern-"+str(i)+".txt.phrase"
    f0=open(outputPath2, 'w')
    with open(outputPath1, 'r') as file:
        for line in file:
            line=line.rstrip()
            support=line.split()[0]
            patterns=line.split()[1:]
            if not patterns:
                pass
            else:
                mappedLine=str(support)+" "
                for pattern in patterns:
                    mappedLine=mappedLine+" "+str(vocabDict[int(pattern)])
                f0.write(mappedLine+"\n")
for i in range(5):
    filename="closed-"+str(i)+".txt"
    outputPath1="./closed/"+filename
    outputPath2="./closed/closed-"+str(i)+".txt.phrase"
    f0=open(outputPath2, 'w')
    with open(outputPath1, 'r') as file:
        for line in file:
            line=line.rstrip()
            support=line.split()[0]
            patterns=line.split()[1:]
            if not patterns:
                pass
            else:
                mappedLine=str(support)+" "
                for pattern in patterns:
                    mappedLine=mappedLine+" "+str(vocabDict[int(pattern)])
                f0.write(mappedLine+"\n")
for i in range(5):
    filename="max-"+str(i)+".txt"
    outputPath1="./max/"+filename
    outputPath2="./max/max-"+str(i)+".txt.phrase"
    f0=open(outputPath2, 'w')
    with open(outputPath1, 'r') as file:
        for line in file:
            line=line.rstrip()
            support=line.split()[0]
            patterns=line.split()[1:]
            if not patterns:
                pass
            else:
                mappedLine=str(support)+" "
                for pattern in patterns:
                    mappedLine=mappedLine+" "+str(vocabDict[int(pattern)])
                f0.write(mappedLine+"\n")
               
for i in range(5):
    filename="purity-"+str(i)+".txt"
    outputPath1="./purity/"+filename
    outputPath2="./purity/purity-"+str(i)+".txt.phrase"
    f0=open(outputPath2, 'w')
    with open(outputPath1, 'r') as file:
        for line in file:
            line=line.rstrip()
            support=line.split()[0]
            patterns=line.split()[1:]
            if not patterns:
                pass
            else:
                mappedLine=str(support)+" "
                for pattern in patterns:
                    mappedLine=mappedLine+" "+str(vocabDict[int(pattern)])
                f0.write(mappedLine+"\n")              