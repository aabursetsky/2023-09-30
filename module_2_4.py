numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes =[]

for i in numbers:
    if i >= 2:
        for j in range(2, i+1):
            if (i % j == 0 and i==j):
                primes.append(i)             # простые числа
                break
            elif (i % j == 0 and i!=j):
                not_primes.append(i)        # составные числа
                break
#             print(i, j)                     # процесс

    elif i < 2:
        not_primes.append(i)                 # если есть 0 или 1
        
print('Primes     : ', primes)    
print('Not Primes : ', not_primes)

# Primes     : [2, 3, 5, 7, 11, 13]
# Not Primes : [1, 4, 6, 8, 9, 10, 12, 14, 15]
