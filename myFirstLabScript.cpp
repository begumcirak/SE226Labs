#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    string name;
    string id;
    cout << "What is your name?" << endl;
    cin >> name;
    cout << "Hello " << name << "." << endl;
    cout << "What is your Student ID?" << endl;
    cin >> id;
    cout << "Your ID is " << id << "." << endl;

    int totalSeconds;
    cout << "Enter total seconds:";
    cin >> totalSeconds;
    int hours = totalSeconds / 3600;
    int minutes = (totalSeconds % 3600) / 60;
    int seconds = totalSeconds % 60;
    cout << totalSeconds << " seconds is " << hours << " hours, " << minutes << " minutes, and " << seconds << " seconds." << endl;

    double x1, y1, x2, y2;
    cout << "Enter x1 and y1:";
    cin >> x1 >> y1;
    cout << "Enter x2 and y2:";
    cin >> x2 >> y2;
    double distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    cout << "Distance: " << distance << endl;

    cout << "Pattern : " << endl;
    cout << "*******\n *****\n  ***\n   *" << endl;

    return 0;
}