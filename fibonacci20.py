def generate_fibonacci(num) :
    fib = list()
    fib.append(0)
    fib.append(1)
    for i in range(2,num) :
        fib.append(fib[i-1] + fib[i-2])
    return fib

N = int(input("enter the number"))
print(generate_fibonacci(N))
