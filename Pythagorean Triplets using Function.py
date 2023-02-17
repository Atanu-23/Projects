m=int(input("Enter lower range: "))
n=int(input("Enter upper range: "))
def pythagorean_triplets(m,n):
    count=0
    while m>=0 and n>0 :
        for a in range(m,n):
            for b in range(a+1,n):
                for c in range(b+1,n+1):
                    if a**2+b**2==c**2 :
                        print("Pythagorean Triplets are: ",a,b,c)
                        count=count+1
        print("Number of Pythagorean Triplets are: ",count)                    
        if count==0:
           print("There is no Pythagorean Triplets!!!")
           break
        break 
    return count
pythagorean_triplets(m,n)         
                
