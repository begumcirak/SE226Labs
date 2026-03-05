n = int(input("Please enter a positive integer greater than 1: "))
steps = 0
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    print(f" -> {n}", end="")
    steps += 1

print(f"\nTotal steps: {steps}")

while True:
    n = int(input("Please enter a number between 10 and 100: "))
    if 10 <= n <= 100:
        break
    print("Invalid input.", end=" ")

fizz_count = 0
buzz_count = 0
fizz_buzz_count = 0

for i in range(1, n + 1):
    if i % 7 == 0:
        print(f"({i} is skipped)" )
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizz_buzz_count += 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(i)

print("Summary")
print(f"Fizz count: {fizz_count}")
print(f"Buzz count: {buzz_count}")
print(f"FizzBuzz count: {fizz_buzz_count}")



while True:
    n = int(input("Please enter a number between 3 and 9: "))
    if 3 <= n <= 9:
        break
    print("Invalid input.", end=" ")

for i in range(1, 2 * n):
    k = n - abs(n - i)
    print("*" * k)