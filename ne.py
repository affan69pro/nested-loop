num=int(input("Enter your number : "))
prime=True
for i in range (2,num):
    if (num % i==0):
        prime=False
        break
if prime==True:
    print("your number is a prime number")
else:
    print("your number is a composite number")