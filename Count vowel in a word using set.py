String=input("Enter the word:")
print()

def CountVowel(String):
    vowel=set("aeiouAEIOU")
    count=0
    for alphabet in String:
        if alphabet in vowel:
            count=count+1
    print("Number of vowel in a word are:",count)
    print("\n")
    
    print("The vowels are:",end="")
    for alphabet in set(String):
        if alphabet in vowel:
            print(alphabet,end=" ")
    print("\n")
    
    print("The frequency of each vowel are:")        
    for alphabet in set(String):
        if alphabet in vowel:
            print(str(alphabet)+":"+str(String.count(alphabet)),end="  ")
        
CountVowel(String)


