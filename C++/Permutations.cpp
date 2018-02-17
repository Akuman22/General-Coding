#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> perm(string& input){                     // Function for deriving permutations
    
    vector<string> listOfPerms, temp, permRet;
    string newInput;
    
    if (input.length() <= 0){               
        permRet.push_back(input);                       // Single Character
        return permRet;
    }

    // Go through each character one by one, and splice string around that character
    for(int i = 0; i<input.length(); i++){  
        newInput = input.substr(0,i)+input.substr(i+1); // Splice at location
        permRet = perm(newInput);                       // Find Permutations of remaining characters

        // Add removed character and add to to the permutations of the remaining characters
        for(int j = 0; j<permRet.size(); j++) {
            listOfPerms.push_back(input[i]+permRet[j]); 
        }
    }
    return listOfPerms;
}

int main() {
    
    vector<string> permutations;
    string input = "abc";
    
    permutations = perm(input);
    for(int i = 0; i<permutations.size(); i++){
        cout << permutations[i] << endl;
    }

    return 0;
}