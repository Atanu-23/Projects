n=int(input("Enter the length of list:"))
wordlist=[]
wordlen=[]
for i in range(n):
    e=input("Enter word"+str(i+1)+":")
    wordlist.append(e)
print("The list of word is: ",wordlist)
def Wordsort(wordlist,wordlen):
    for i in wordlist:
        wordlen.append((len(i),i))
    wordlen.sort()
    return wordlen[-1][1]
Wordsort(wordlist,wordlen)
print("The maximum length of word is:",wordlen[-1][1])
print("\n")
print("The length of word "+wordlen[-1][1]+" is: ",len(wordlen[-1][1]))

