a =  int(input('unesite staranicu a:'))
b =  int(input('unesite staranicu b:'))
c =  int(input('unesite staranicu c:'))

print ('stranice trougla su:',a,',',b,',',c)

if a+b>3 and a+c>b and b+c>a :
    print ("trougao postoji")

    if a==b and b!=c:
        print('trougao je jednakokraki')
    if c==a and b!=a:
        print('trougao je jednakokraki')
    if b==c and b!=a:
        print('trougao je jednakokraki')
    if b==a and b==c:
        print('trougao je jednakostranicni')
    if a!=b and b!=c and a!=c:
        print('trougao je raznostranican')

else :
    print('trougao nepostoji')