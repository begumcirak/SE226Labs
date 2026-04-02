
def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


term_calc = lambda x, i: (x**i) / factorial(i)

def exp_x(x, n):
    result = 0

    for i in range(n):
        result += term_calc(x, i)
    return result


total_sum = 0

def solve_series_recursive(n):

    """
        Logic: The function calls itself by decrementing n until it reaches 0 (base case).
        Sign Handling: The formula (-1)^(n+1) ensures that terms with odd denominators
        are positive and terms with even denominators are negative.
        The function returns nothing; it updates the global variable 'total_s'.
        """

    global total_sum
    if n > 0:

        term = ((-1)**(n + 1)) / n
        total_sum += term
        solve_series_recursive(n - 1)


if __name__ == "__main__":

    user_x = float(input("Enter the value for x: "))
    user_n = int(input("Enter the number of terms (n): "))
    print(f"e^{user_x} (for {user_n} terms): {exp_x(user_x, user_n)}")


    n_val = int(input("\nEnter n for the alternating series S_n: "))
    solve_series_recursive(n_val)
    print(f"Sum of S_{n_val}: {total_sum}")