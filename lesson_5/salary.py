
i = 0 
primes = list()
while i < 100:
    i += 1

    int_match = 0 
    start = 1 
    
    if (i / 2).is_integer() == False: 
        while i > start: 
            start += 1
            if (i / start).is_integer() == True: 
                print(i)
                int_match += 1

    if int_match == 1:
        primes.append(i) 
print(primes)

i=1
while i<100:
    i += 1
    j=2
    is_prime=True
    while j < i:
        if i%j==0:
            is_prime=False
            break
        j+=1
    if is_prime:
        print(j)
    
    