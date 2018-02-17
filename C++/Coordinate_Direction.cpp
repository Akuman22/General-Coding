/*
 * Given two graph points determine in what direction (N, NE, NW, E, W, S, SE, SW)
 * the second point is from the first and display.
 * If points are the same display here.
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    // Read lines one by one
    while (getline(stream, line)) {
        vector<int> numbers;                        // Vector to store numbers
        int sum = 0;                                // Variable to keep track of numbers
        for(int i = 0; i<line.length(); i++) {
            if (line[i] == ' ') {                   // Space denotes new number
                numbers.push_back(sum); 
                sum = 0;
            } else if (isdigit(line[i])) {
                sum = (sum * 10) + (int)line[i];  // 123 = 1*100 + 2*20 + 3; Ascii 0 = 48
            }
            else{
                break;
            }
        }
        numbers.push_back(sum);                     // Final number
        string outPut = "";                         // Initialize Output 
        // Just in case of invalid input
        if(numbers.size() == 4){
            if(numbers[1] != numbers[3]) {          // Y axis is not the same
                if (numbers[1] > numbers[3])        
                    outPut += "N";
                else
                    outPut += "S";
            }
            if(numbers[0] != numbers[2]) {          // X axis is not the same
                if (numbers[0] > numbers[2])
                    outPut += "E";
                else
                    outPut += "W";
            }
            // If none of the above conditions are true, print Same.
            cout<< (outPut.length()==0?"Same":outPut) << endl;
        }
        else{
            cout << "Insufficient Numbers";
        }
    }
    return 0;
}