a=int(input("enter no:"))
notes=n_2000=n_500=n_100=n_50=n_20=n_10=0
if a>=2000:
    n_2000=a//2000
    a=a-(n_2000)*2000
    print(2000,"=",n_2000)
if a>=500:
    n_500=a//500
    a=a-(n_500)*500
    print(500,"=",n_500)
if a>=100:
    n_100=a//100
    a=a-(n_100)*100
    print(100,"=",n_100)
if a>=50:
    n_50=a//50
    a=a-(n_50)*50
    print(50,"=",n_50)
if a>=20:
    n_20=a//20
    a=a-(n_20)*20
    print(20,"=",n_20)
if a>=10:
    n_10=a//10
    a=a-(n_10)*10
    print(10,"=",n_10)
else:
    print("0")    