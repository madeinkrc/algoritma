sayi=input("sayi giriniz: ")
i=1
T=0
for i in range(i,sayi-1):
    if sayi%i==0:
        T=T+i

if T==sayi:
    print (sayi), "mukemmel sayi"
else:
    print "mukemmel degil"
