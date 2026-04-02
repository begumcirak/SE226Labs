#include <iostream>

using namespace std;


double solveSeriesRecursive(int n) {

    
    if (n == 1) {
        return 1.0;
    }

    double sign = (n % 2 == 0) ? -1.0 : 1.0;
    double currentTerm = sign / n;


    return currentTerm + solveSeriesRecursive(n - 1);
}

int main() {
    int n;
    cout << "Enter the value for n: ";
    cin >> n;

    if (n <= 0) {
        cout << "Please enter a positive integer." << endl;
    } else {
        double result = solveSeriesRecursive(n);
        cout << "The sum of the series S_" << n << " is: " << result << endl;
    }

    return 0;
}