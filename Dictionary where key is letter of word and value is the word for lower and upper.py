String=input("Enter String:")
words=String.split()
dictionary={}

for word in words:
    if word[0].lower() not in dictionary.keys():
        dictionary[word[0].lower()]=[]
        dictionary[word[0].lower()].append(word)
    else:
        if word not in dictionary[word[0].lower()]:
            dictionary[word[0].lower()].append(word)
print("The dictionary made of letter of word as key and words as value is:",dictionary)            
