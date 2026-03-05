#include <iostream>
using namespace std;

int main() {
    int x;
    int steps = 0;
    cout << "Please enter a positive integer greater than 1: ";
    cin >> x;

    cout << x;
    while (x != 1) {
        if (x % 2 == 0) {
            x /= 2;
        } else {
            x = x * 3 + 1;
        }
        cout << " -> " << x;
        steps++;
    }
    cout << "\nTotal steps: " << steps << endl;


    int n;
    while (true) {
        cout << "Please enter a number between 10 and 100: ";
        cin >> n;
        if (n >= 10 && n <= 100) break;
        cout << "Invalid input. ";
    }

    int fizz = 0, buzz = 0, fizzbuzz = 0;

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) {
            cout << "(" << i << " is skipped)" << endl;
            continue;
        }
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        } else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        } else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        } else {
            cout << i << endl;
        }
    }

    cout << "Summary" << endl;
    cout << "Fizz count: " << fizz << endl;
    cout << "Buzz count: " << buzz << endl;
    cout << "FizzBuzz count: " << fizzbuzz << endl;



        int a;

        while (true) {
            std::cout << "Please enter a number between 3 and 9: ";
            std::cin >> a;
            if (a >= 3 && a <= 9) {
                break;
            }
            std::cout << "Invalid input. ";
        }

        for (int i = 1; i <= 2 * a - 1; i++) {
            int k = a - std::abs(a - i);
            for (int j = 0; j < k; j++) {
                std::cout << "*";
            }
            std::cout << std::endl;
        }

        return 0;
    }







