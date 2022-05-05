from datetime import datetime







def get_primes(upper_limit):
    # Initialize the list of primes for the basic ones
    primes = [2]

    for i in range(3, upper_limit, 2):
        is_prime = True
        for div in primes:
            # print('i=' + str(i) + ' div=' + str(div))
            # print(primes)
            # If a prime gives a zero modulus, i is not prime
            if i % div == 0:
                is_prime = False
                break

            # Once 1/3 through the list of primes, you don't need do continue
            # if div > i/3:
            #     # print('  i=' + str(i))
            #     # print('     div=' + str(div))
            #     break

        if is_prime:
            primes.append(i)
            # print(i)

    return len(primes)


upper_limits = [10000]
results = []
found = []

for limit in upper_limits:

    # Save starting time
    start = datetime.today()

    found.append(get_primes(limit))

    # Save ending time
    end = datetime.today()

    # elapsed time
    elapsed = end - start
    results.append(elapsed.total_seconds())
    #print(elapsed.total_seconds())

    # print("Found " + str(total) + " prime numbers less than " + str(limit) + ' in ' + str(elapsed.total_seconds())  + ' seconds\n')
    # print(elapsed.total_seconds())

print(results)
print(found)

