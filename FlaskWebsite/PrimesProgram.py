


import datetime



a, b, i, j, flag = 0, 0, 0, 0, 0
 
a = int(0)
     
print('Welcome to the prime number finding program! Lower interval is set to 0.')
print('Enter upper bound of the interval below 10000: ')


begin_time = datetime.datetime.now()
if b > 10000:
    print('\nPlease enter a value below 10,000.')
    
else:     
    primes = []
 
    print('\nYour prime numbers between', a, 'and', b, 'are: ', end = '')
    for i in range(a, b + 1):

            if (i == 1):
                continue

            flag = 1
            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    flag = 0
                    break     

            if (flag == 1):
                print(i, end = " ")
                primes.append(i)
                
            
                
print('\nThe program took',datetime.datetime.now() - begin_time,'to execute.')
                
                
