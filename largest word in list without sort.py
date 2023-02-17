n=int(input("Enter the length of list:"))
wordlist=[]
wordlenlist=[]
for i in range(n):
    element=input("Enter word"+str(i+1)+":")
    wordlist.append(element)
print("The list of word is:",wordlist)
largest=len(wordlist[0])
temp=wordlist[0]

def LargestWord(wordlist,wordlenlist,largest,temp):
    for word in wordlist:
        if len(word)>largest:
            largest=len(word)
            temp=word       
    print("The larget word in the wordlist is:",temp,end=" ")
    print("and its length is:",largest)
LargestWord(wordlist,wordlenlist,largest,temp)

            
