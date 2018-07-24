a = input ('zelite li da mnozite brojeve da/ne:')

if a == 'da':
    b = int(input('unesite prvi broj:'))
    if b <= 10:
        c = int(input('unesite drugi broj:'))
        if c <= 10:
            d = b*c 
            print ("umnozak brojeva je :", d)
        else:
            print("broj nije u rasponu <= 10")
    else:
        print("broj nije u rasponu <= 10")
else:
    print("izlazak iz programa")

    