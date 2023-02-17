n=int(input("Enter length of wordlist:"))
wordlist=[]
norepeatwordlist=[]
for i in range(n):
    e=input("Enter element"+str(i+1)+":")
    wordlist.append(e)
print("The list of word is:",wordlist)
print("\n")
def NoRepeatingWord(wordlist,norepeatwordlist):
    for word in wordlist:
        if word not in norepeatwordlist:
            norepeatwordlist.append(word)
    print("The list with no repeated word is:",norepeatwordlist)
NoRepeatingWord(wordlist,norepeatwordlist)    
