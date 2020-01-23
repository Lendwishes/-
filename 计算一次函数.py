xuna = int(0)
while xuna < 1:
    xunb = int(0)
    ax = float(input("X1="))
    ay = float(input("Y2="))
    bx = float(input("X2="))
    by = float(input("Y2="))
    print("running...")
    linsq = by - ay
    linsw = bx - ax
    k = linsq / linsw
    linse = ax * k
    b = ay - linse 
    if b > b:
        print("result:y="+str(k)+"x+"+str(b))
    elif b < 0:
        print("result:y="+str(k)+"x-"+str(b))
    elif b == 0:
        print("result:y="+str(k)+"x")
