def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def main():
    n = int(input("Enter the upper limit for Fibonacci sequence: "))
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence up to", n, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
