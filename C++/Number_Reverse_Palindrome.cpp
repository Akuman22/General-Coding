/*
 * Given an initial number, reverse it and add it back to the initial.
 * Check if new number is a palindrome.
 * If not repeat till is.
 * If yes display how many iterations it took and the number.
*/
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Function to check for Number Palindromes
void palindrome(vector<int> numbers, int rep){
    if(numbers.size() == 0)return;              // Empty number
    if (rep>=1000){                             // If reps have gone beyond 1000, assume no palindrome
        cout << "No Palindrome"<<endl;
        return;
    }
    vector<int> revNumber, newNumber;
    int carry = 0, sum = 0;
    revNumber = numbers;
    if(numbers.size()>1)                        // More than single digit
        reverse(numbers.begin(), numbers.end());
    if(revNumber == numbers){                   // If palindrome
        cout << rep << " ";                     // Number of iterations it took
        for(int i = 0; i<numbers.size();i++){
            cout << numbers[i];                 // Print the number
        }
        cout << endl;
        return;
    }
    for(int i = 0; i<numbers.size(); i++){
        sum = numbers[numbers.size()-1-i] +     // sum = digit 1 + digit 2 + carry from lower digit
                revNumber[numbers.size()-1-i] +
                carry;
        carry = 0;
        if(sum >=10){
            sum = sum%10;
            carry = 1;
        }
        newNumber.push_back(sum);               // Add digit to new number
    }
    if(carry == 1){                             // Extra digit required
        newNumber.push_back(carry);
    }
    reverse(newNumber.begin(), newNumber.end());// Vector is built in reverse, so reversing it will correct the order
    palindrome(newNumber, rep+1);               // Recurr with new Number and increment iteration.
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> numbers;                    // Vector to store numbers
        for(int i = 0; i<line.length(); i++) {  // Read the number, character by character.
            if(isdigit(line[i])){
                numbers.push_back(line[i] - 48);// In ASCII, '0' = 48
            }
            else
                break;                          // Invalid input
        }
        palindrome(numbers, 0);
    }
    return 0;
}
