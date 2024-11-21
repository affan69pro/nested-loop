start=int(input("Enter your starting value: "))
end=int(input("Enter your end number: "))
for j in range(start,end+1):
    prime=True
    for i in range(2,j):
        if (j % i==0):
            prime = False
            break
    if prime==True:
        print(j,end=" ")