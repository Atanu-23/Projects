String=input("Enter the Word:")
count=0
def CountVowel(String,count):
    for item in String:
        if(item=='A' or item=='E' or item=='I' or item=='O' or item=='U' or item=='a' or item=='e' or item=='i' or item=='o' or item=='u'):
            count=count+1
    print("The  number of vowels in the word is:",count)
CountVowel(String,count)
