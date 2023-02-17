lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))

def IsPalindrom(n):
    rev=0
    d=0
    m=n
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return (m==rev)

def CountPalindrom(l,u):
    for i in range(l,u+1):
        if IsPalindrom(i) and i%2!=0:
            print(i,end=" ")

if __name__=="__main__":
    CountPalindrom(lower,upper)
