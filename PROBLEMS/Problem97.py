#Find the count of prime numbers in the array. 
def countprime(num):
    count = 0

    for n in num:
        if n <= 1:
            continue   
        is_prime = True
        for j in range(2, n):
            if n % j == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count


num = [1,2,3,4,5,6,7,8,9,10]
print(countprime(num))