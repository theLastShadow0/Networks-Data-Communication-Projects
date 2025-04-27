#include <iostream>
#include <string>
#include <vector>

using namespace std;

//D(X) = (X - B) * a^-1 mod 26
void decryptCipherText(vector<char> cipherText, int B, int A, vector<char> alphabet){
    int inverse_A = 1;
    int num = 0;
    int alphabetSize = 26;
    int mod_mult = 1;
    int mod_result = 1;
    int decryption;
    int X = 0;
    vector<char> plainText= {};
    string result;
    
    //Obtaining the inverse of A to use for decryption
    //A * inverse of A should be one digit higher than alphabet size (For example: 27,26 mod(27,26) = 1)
    while (num % mod_result != 1){
        num = A * inverse_A;
        mod_result =  alphabetSize * mod_mult; 
        if (num < mod_result){
            inverse_A++;
        }
        else{
            mod_mult++;
        }
    }

    for (int i = 0; i < cipherText.size(); i++){
        for (int j = 0; j < 26; j++){

            if (cipherText[i] == alphabet[j]){
                 X = j;
                 int sum = (X - B) * inverse_A;

                 if (sum < 0){
                   decryption = 26 -(abs(sum) % 26);  
                 }
                 else {
                     decryption = sum % 26;
                 }

                 plainText.push_back(alphabet[decryption]);
                 cout << "Decryption: " << "(X - B)* a^-1 mod 26" << endl;
                 cout << X << " - " << B << " * " << inverse_A << " mod 26 = " << decryption << "(" << alphabet[decryption] << ")" << endl;
                 break;
            }
        }
    }
    for (char c: plainText){
        result += c;
    }
    cout << "The decrypted ciphertext is: " << result << endl;
}

int main(){
    // Encryption = A * X + B (mod 26)
    int A;
    int B;
    int X;

    int encryption;
    string plainText;
    int invalidValues[] = {2,4,6,8,10,12,13,14,16,18,20,22,24}; //Value A has to be coprime to the alphabet
    vector<char> alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    vector<char> cipherText = {};
    string result;
    char input;

    cout << "Enter key coefficients A and B: \n A: ";
    cin >> A;
    cout << " B: ";
    cin >> B;


    for (int i = 0; i < 13; i++){
        if (A == invalidValues [i]){
            cout << "Value A has to be coprime to the alphabet. Try again." << endl;
            return 0;
        }
    }
    cin.ignore(); //ignores end line so plain text cannot be empty

    cout << "Please enter a text you would like to have encrypted: " << endl;
    getline (cin, plainText);

    //Encryption and Output
    for (int i = 0; i < plainText.length(); i++){
        for (int j = 0; j < 26; j++){
            if (plainText[i] == alphabet[j]){
                X = j;
                encryption = (A * X + B) % 26;
                cipherText.push_back(alphabet[encryption]);
                cout << "Encryption: " << "(A * X + B) mod 26" << endl;
                cout << A << " * " << X << " + " << B << " mod 26 = " << encryption << "(" << alphabet[encryption] << ")"<< endl;
                break;
            }
        }
    }
    for (char c: cipherText){
        result += c;
    }
    cout << "The plaintext safely encrypted to: " << result << endl;
    cout << endl;
    cout << "Would you like to decrypt the ciphertext (y/n)?" << endl;
    cin >> input;

    switch(input){
        case 'y':
        decryptCipherText(cipherText, B, A, alphabet);
        break;

        case 'n':
        cout << "Goodbye" << endl;
        break;
    }
}

