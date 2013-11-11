
import re
import sys
from operator import itemgetter
from itertools	 import chain, combinations
from collections import defaultdict
from sys import argv
import math
from collections import OrderedDict

def extractTransaction(fname):
	f4= open(fname, 'rU')
   	for line in f4:
		line = line.strip().rstrip(',')		
		transaction= frozenset(line.split(' '))
		yield transaction

def itemsSatisfyingSupport(transactions,items,frequentSet,minSupport):
    local = defaultdict(int)
    _items = set()
    for item in items:
        for transaction in transactions:
            if item.issubset(transaction):
                local[item]  += 1
                frequentSet[item]   += 1
                
 
    for item,num in local.items():
        sup = float(num)/len(transactions)
        if sup >= minSupport:
            _items.add(item)
    
    return _items


def aprioriFrequentPatternMining(transactionInput,min_support):
   
    size = 2 #begin with sets of size 2
    iSet   = set()
    transactions    = list()
    for i in transactionInput:
        transaction = frozenset(i)
        transactions.append(transaction)
        for item in transaction:
            iSet.add(frozenset([item]))


    frequentSet     = defaultdict(int)  
        
    singleCandidateSet     = itemsSatisfyingSupport(transactions,iSet,frequentSet,min_support)

    LItemSet = singleCandidateSet # Start with single candidates
    
    tempSet        = dict() 
    while(LItemSet != set([])):   #keep reducing till it becomes a null set

        tempSet[size-1] = LItemSet #copy it and store it temporarily
        LItemSet      = join(LItemSet,size) # perform join
        CandidateSet  = itemsSatisfyingSupport(transactions,LItemSet,frequentSet,min_support) #mine the CandidateSet of size k

        LItemSet      = CandidateSet #reinitialize LItemSet with the Candidate Set generated

        size = size + 1

    frequentItems=[] #start Generating Frequent items here

    for key,value in tempSet.items():
        frequentItems.extend([(tuple(item),float(frequentSet[item])/len(transactions)) 
                           for item in value])
    return frequentItems

def join(itemSet,length):
    joinResult=set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])
    return joinResult

def subsets(arr):
    ret=chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])
    return ret

def subsets2(mySet):
    return reduce(lambda z, x: z + [y + [x] for y in z], mySet, [[]])

def findClosedPatterns(items,index):
    sorted_items= sorted(items,key=itemgetter(1),reverse=True)
    allSet= set()
    seenSet=set()
    dictItems=dict(sorted_items)
    outputPath="./pattern/closed-"+str(index)+".txt"
    f2=open(outputPath, 'w+')
    for k in dictItems.keys():
        allSet.add(k)
    #print allSet
    closedPatternList=list()
    for i in allSet:
        if i not in seenSet:
            candidateSet=set()
            candidateSet.add(i)
            diffSet = set()
            diffSet=allSet
            #f2.write(str(i)+"\n")
            seenSet.add(i)
            diffSet = diffSet.difference(candidateSet)
            flagPossibleClosedPattern=0
            flagNotClosedPattern=0;
            for k in diffSet:
                kItemSet=set()
                for term in str(k).split():
                    kItemSet.add(term)
                if candidateSet  in subsets2(kItemSet):
                    flagPossibleClosedPattern=1
                    if float(dictItems[i]) == float(dictItems[k]):
                        flagNotClosedPattern=1;
                    else:
                        closedPatternList.append(candidateSet)
                if flagNotClosedPattern==0 :
                    closedPatternList.append(candidateSet)
    patternDict= {}       
    filename="pattern-"+str(index)+".txt"
    outputPath1="./pattern/"+filename 
    with open(outputPath1, 'r') as file:
        for line in file:
            support=line.split()[0]
            phrase=line.split()[1:]
            key=""
            for word in phrase:
                key=key+word+" "
            key=key.rstrip()
            patternDict[str(key)]=support     
    for key in uniq(closedPatternList):
        f2.write(patternDict[str(re.sub('[^0-9 ]','',str(key))).strip(',')]+" "+str(re.sub('[^0-9 ]','',str(key))).strip(',')+"\n")
def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output
def findMaximalPatterns(items,index):
    sorted_items= sorted(items,key=itemgetter(1),reverse=True)
    allSet= set()
    seenSet=set()
    dictItems=dict(sorted_items)
    outputPath="./pattern/max-"+str(index)+".txt"
    f1=open(outputPath, 'w+')
    for k in dictItems.keys():
        allSet.add(str(re.sub('[^0-9 ]','',str(k))).strip(','))
    #print allSet
    maxPatternList=list()
    for i in allSet:
        if i not in seenSet:
            candidateSet=set()
            candidateSet.add(i)
            diffSet = set()
            diffSet=allSet
            seenSet.add(i)
            diffSet = diffSet.difference(candidateSet)
            flagNotMaximal=0
            for k in diffSet:
                kItemSet=set()
                for term in str(k).split():
                    kItemSet.add(term)
                if candidateSet  in subsets2(kItemSet):
                    flagNotMaximal=1
                    break;
            if flagNotMaximal ==0:
                maxPatternList.append(candidateSet)
    patternDict= {}       
    filename="pattern-"+str(index)+".txt"
    outputPath1="./pattern/"+filename 
    with open(outputPath1, 'r') as file:
        for line in file:
            support=line.split()[0]
            phrase=line.split()[1:]
            key=""
            for word in phrase:
                key=key+word+" "
            key=key.rstrip()
            patternDict[str(key)]=support
    for key in maxPatternList:
        f1.write(str(patternDict[str(re.sub('[^0-9 ]','',str(key))).strip(',')])+" "+str(re.sub('[^0-9 ]','',str(key))).strip(',')+"\n")


def purityCalc(items):
    count=len(items)
    l=[]
    for i in range(count):
        t={}
        tempList=[]
        tempList=items[i]
        for (n,v) in tempList:
            t[n] = v  
        l.append(t)
    supportItemsDictList=l
    weightedSupportPurityItemsDictList=l
    purityItemsDictList=l
    for i in range(count):
        tempDict={}
        tempDict=l[i]
        for key in tempDict:    
            tempDict[key]=evalPurity(i,key,supportItemsDictList)
        purityItemsDictList[i]=tempDict
    sorted_weightedSupportPurityItemsDictList =[]
    for i in range(count):
        for key in weightedSupportPurityItemsDictList[i]:
            weightedSupportPurityItemsDictList[i][key]=(purityItemsDictList[i][key]*(1+float(supportItemsDictList[i][key])))
        purityFileName="purity-"+str(i)+".txt"
        purityPath="./pattern/"+purityFileName
        f5=open(purityPath, 'w+')
        sorted_weightedSupportPurityItemsDictList.append(OrderedDict(sorted(weightedSupportPurityItemsDictList[i].items(), key=itemgetter(1),reverse=True)))
        for key in sorted_weightedSupportPurityItemsDictList[i]:
            f5.write("%0.4f %s \n" % (sorted_weightedSupportPurityItemsDictList[i][key],str(re.sub('[^0-9 ]','',str(key))).strip(',')))


    
        

def evalPurity(i,n,supportItemsDictList):
    ftdt=supportItemsDictList[i][n]
    dt=[9411,8375,8453,8524,8633]
    secondTerm=0
    for j in range(5):
        tempDict={}
        tempDict=supportItemsDictList[j]
        if j==i:
            pass
        else:
            try:
                tft=tempDict[n]*dt[j]
            except KeyError:
                tft=0
            temp=(ftdt*dt[i]+tft)/calcDTxDTy(i,j)
            if temp>secondTerm:
                secondTerm=temp
    if secondTerm == 0:
        secondTerm=1
    purity=math.log(abs(ftdt)/abs(secondTerm))
    return purity

def calcDTxDTy(x,y):
    with open('word_assignment_stripped.dat', 'r') as file:
        counter=0
        for line in file:
            words=line.split()
            for word in words:
                tup=word.split(':')
                if int(tup[1]) in [x,y]:
                    counter+=1
    if counter==0:
        return  1
    else:
        return counter

def outputPatterns(items,outputfile,index):
    sorted_items= sorted(items,key=itemgetter(1),reverse=True)
    vocabDict= {}
    iterator=0     
    outputPath1="./pattern/"+outputfile
    f0=open(outputPath1, 'w+')
    for item,support in sorted_items:
         f0.write("%0.4f %s \n" % (support,str(re.sub('[^0-9 ]','',str(item))).strip(',')))  

if __name__ == "__main__":
    name,min_support=argv
    indices=[0,1,2,3,4]
    purityItems=[]
    for index in indices:
        transactionInput=extractTransaction("topic-"+str(index)+".txt")
        items={}
        items= aprioriFrequentPatternMining(transactionInput,float(min_support))
        purityItems.append(items)
        outputFileName="pattern-"+str(index)+".txt"
        outputPatterns(items,outputFileName,index)
        findMaximalPatterns(items,index)
        findClosedPatterns(items,index)
    purityCalc(purityItems)

    print "program complete"


