pares = input()

for i in range(0, pares):
    a, b = input()  
    print(a)
    print(b)
    while (b != 0):
        r = a % b
        a = b
        b = r
        print(r)
    print("---")
