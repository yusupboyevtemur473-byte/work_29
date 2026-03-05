#11-misol
#n = int(input("n = "))
#k = 0
#s = 0
#while s < n:
#    k += 1
#    s += k
#print("Eng kichik k =", k)
#print("Yig'indi =", s)

#12-misol
#n = int(input("n = "))
#k = 0
#s = 0
#while s + (k + 1) <= n:
#    k += 1
#    s += k
#print("Eng katta k =", k)
#print("Yig'indi =", s)

#13-misol
#a = float(input("a = "))
#k = 0
#s = 0
#while s < a:
#    k += 1
#    s += 1 / k
#print("Eng kichik k =", k)
#print("Yig'indi =", s)

#14-misol
#a = float(input("a = "))
#k = 0
#s = 0
#while s + 1/(k + 1) <= a:
#    k += 1
#    s += 1/k
#print("Eng katta k =", k)
#print("Yig'indi =", s)

#15-misol
#S = float(input("Boshlang'ich summa = "))
#p = float(input("Foiz = "))
#k = 0

#while S <= 2:
#    S = S * (1 + p/100)
#    k += 1

#print("Oylar soni =", k)
#print("Yakuniy summa =", S)
#16-misol
#p = float(input("Foiz = "))
#kun = 1
#masofa = 10
#jami = 10

#while jami <= 200:
#    masofa = masofa * (1 + p/100)
#    jami += masofa
#    kun += 1

#print("Kunlar soni =", kun)
#print("Jami masofa =", int(jami))
#17-misol
#n = int(input("n = "))
#m = int(input("m = "))

#butun = 0
#qoldiq = n

#while qoldiq >= m:
#    qoldiq -= m
#    butun += 1

#print("Butun qism =", butun)
#print("Qoldiq =", qoldiq)
#18-misol
#n = int(input("n = "))
#teskari = 0

#while n > 0:
#    qoldiq = n % 10
#    teskari = teskari * 10 + qoldiq
#    n //= 10

#print("Teskari son =", teskari)
#19-misol
#n = int(input("n = "))
#yigindi = 0
#soni = 0

#while n > 0:
#    yigindi += n % 10
#    soni += 1
#    n //= 10

#print("Raqamlar yig'indisi =", yigindi)
#print("Raqamlar soni =", soni)
#20-misol
#n = int(input("n = "))
#bor = False

#while n > 0:
#    if n % 10 == 2:
#        bor = True
#    n //= 10
#print("2 raqami bor:", bor)

