def CountCharacter(Word,ch):
    if not Word:
        return 0
    elif(Word[0]==ch):
        return 1+CountCharacter(Word[1:],ch)
    else:
        return CountCharacter(Word[1:],ch)
Word=input("Give a word:")
ch=input("Give the character you want to find:")
print("The frequency of character you want to find is:",end="")
print(CountCharacter(Word,ch))
