fib1=1
fib2=1

sayi=input("sayi gir ")

if fib1==1:
    print ("1")
if fib2==1:
    print ("1")
for i in range(3,sayi+1):
   

    fib=fib1+fib2
    fib1=fib2
    fib2=fib

    print fib
