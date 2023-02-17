String=input("Enter String:")
words=String.split()
print(words)
dictionary={}
for word in words:
    if word[0]not in dictionary.keys():
        dictionary[word[0]]=[]
        dictionary[word[0]].append(word)
    else:
        if word not in dictionary[word[0]]:
            dictionary[word[0]].append(word)

print("The dictionary of letter of word as key and word as value is:",dictionary)             
