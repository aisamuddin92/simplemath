def OscillateLeibnizPi():
    i_calculations = int(input("How many calculations would you like to do? "))
    pi = 0.0
    for i_num in range(i_calculations):
        pi += ((1 / ((2*i_num)+1))*((-1)**i_num))*4
        print(pi)

def ConvergeLeibnizPi():
    i_calculations = int(input("How many calculations would you like to do? "))
    pi = 0.0
    for i_num in range(i_calculations):
        old_pi = pi
        pi += ((1 / ((2*i_num)+1))*((-1)**i_num))*4
        print((old_pi+pi)/2)

def CalculatePrimes():
    i_calculations = int(input("Find all of the primes up to ...? "))
    l_primes = [2]
    print(2)
    for i_num in range(3,i_calculations):
        b_prime = True
        for i_prime in l_primes:
            if i_num % i_prime == 0:
                b_prime = False
        if b_prime == True:
            l_primes.append(i_num)
            print(i_num)

def CalculateFibonacci():
    i_fibs = int(input("Find how Fibonacci numbers? "))
    l_fibs = [1,1]
    print("1\n" + "1")
    for i_fib in range(i_fibs-2):
        l_fibs.append(l_fibs[-1]+l_fibs[-2])
        print(l_fibs[-1])

def OscillateNilakanthaPi():
    pi = 3 # 661
    i_calcs = int(input("How many calculations would you like to do?"))
    n = 2
    for i_calc in range(i_calcs):
        pi += (4 / (n*(n+1)*(n+2)))*(-1)**i_calc
        print(pi)
        n += 2
        
def ConvergeNilakanthaPi():
    pi = 3
    i_calcs = int(input("How many calculations would you like to do?"))
    n = 2
    for i_calc in range(i_calcs):
        old_pi = pi
        pi += (4 / (n*(n+1)*(n+2)))*(-1)**i_calc
        print((old_pi+pi)/2)
        n += 2
##    i_correct_digits = CorrectDigits(pi)
##    print("You successfully calculated " + str(i_correct_digits) + "correct digits of pi.")

def RegularEuclideanAlg():
    print("\nGiven nonnegative integers m and n that are both not zero, the Euclidian Algorithm computes the greatest common denominator of m and n.")
    m = int(input("Enter integer m. "))
    n = int(input("Enter integer n. "))
    l_rems = [m,n]
    i = 1
    while l_rems[i] != 0:
        i+= 1
        l_rems.append(l_rems[i-2] % l_rems[i-1])
        print(l_rems[i])
    print("The greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(l_rems[i-1]) + ".\n")

def ExtendedEuclideanAlg():
    print("\nGiven nonnegative integers m and n, not both zero, this algorithm computes gcd(m,n) and also integers x and y such that mx + ny = gcd(m,n).")
    m = int(input("Enter integer m. "))
    n = int(input("Enter integer n. "))
    l_rems = [m,n]
    l_x = [1,0]
    l_y = [0,1]
    i = 1
    while l_rems[i] != 0:
        i += 1
        q = l_rems[i-2] // l_rems[i-1]
        l_rems.append(l_rems[i-2] % l_rems[i-1])
        l_x.append(l_x[i-2] - (q * l_x[i-1]))
        l_y.append(l_y[i-2] - (q * l_y[i-1]))
        print("r = " + str(l_rems[i]) + ", q = " + str(q) + ", x = " + str(l_x[i]) + ", y = " + str(l_y[i]))
    print("gcd(" + str(m) + "," + str(n) + ") = " + str(l_rems[i-1]) + " = " + str(m) + "(" + str(l_x[i-1]) + ") + " + str(n) + "(" + str(l_y[i-1]) + ").\n")

def main():
    while True:
        print("1 - Calculate Pi with Leibniz Series - Oscillates\n" + "2 - Calculate Pi with Leibniz Series - Converges\n" + "3 - Calculate Prime Numbers\n" + \
              "4 - Calculate Fibonacci Numbers\n" + "5 - Calculate Pi with Nilakantha Series - Oscillates\n" + "6 - Calculate Pi with Nilakantha Series - Converges\n" + \
              "7 - Execute Euclidean Algorithm")
        i_num = int(input("8 - Execute Extended Euclidean Algorithm "))
        if i_num == 1:
            OscillateLeibnizPi()
        if i_num == 2:
            ConvergeLeibnizPi()
        if i_num == 3:
            CalculatePrimes()
        if i_num == 4:
            CalculateFibonacci()
        if i_num == 5:
            OscillateNilakanthaPi()
        if i_num == 6:
            ConvergeNilakanthaPi()
        if i_num == 7:
            RegularEuclideanAlg()
        if i_num == 8:
            ExtendedEuclideanAlg()

main()
