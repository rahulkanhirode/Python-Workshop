def substraction(p):
    while (p > 0):  
        q = p
        s = 0
        while (q > 0):
            s = s + ( q % 10 )
            q = int ( q / 10 )
        print(p)
        p -= s
q =int(input("Enter a positive number "))
substraction(q)
