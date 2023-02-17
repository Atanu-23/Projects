String=input("Enter the word:")
string=String




def CountWord(String):
    dictionary={i: String.count(i) for i in set(String)}
    print("The dictionary made from letter of word is",dictionary)
CountWord(String)




def CountFrequency(string):
    dictionary={}
    for key in string:
        dictionary[key]=dictionary.get(key,0)+1
    print("The dictionary made from letter of word is",dictionary)
CountFrequency(string)

    
