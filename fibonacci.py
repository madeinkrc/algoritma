sayi=input('kacinci fib  =')
if sayi<=0:
    print('fib sayilari 1. den baslar tekrar deneyin   ')

fib1=1
fib2=1
if sayi==1:
    print fib1,(' dir')
if sayi==2:
    print fib2,(' dir')

for i in range(2,sayi):
    fib=fib1+fib2
    fib1=fib2
    fib2=fib

print fib,(' dir')
