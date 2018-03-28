pares = input()

for k in range(0, pares):
    
    a, b = input()
    i = 0
    
    while a-(b*i) > 0:
        resto = int((a-(i*b)))
        dividindo = int(i*b)
        quociente = int(i)
        print("%d %d" % (quociente, resto))
        i=i+1
    print("---")
