#include <iostream>
#include <string>

using namespace std;

void SWAP_SERVER (string& TAM_TAB_SERVER, char i , char j){
    if (i != j){
        char temp = TAM_TAB_SERVER[i];
        TAM_TAB_SERVER[i] = TAM_TAB_SERVER[j];
        TAM_TAB_SERVER[j] = temp;
    }
}

int main(){
    string TAM;
    string TAM_TAB_CLIENT;
    string TAM_TAB_SERVER;
    int low =0;
    int mid =0;

    cout << "Please enter a sequence of only T, A, M characters ending with a #: " << endl;
    getline(cin,TAM);

    if (TAM.empty() || TAM[0] == '#'){
        cout << "Empty input. Try Again." << endl;
        return 0;
    }
    else if (TAM.find(' ') != string::npos){
        cout << "No spaces allowed. Try Again." << endl;
        return 0;
    }
    else {
        TAM_TAB_CLIENT = TAM;
        TAM_TAB_SERVER = TAM_TAB_CLIENT;
        int high = TAM_TAB_SERVER.length() - 2;

        while(mid <= high){
            if (TAM_TAB_SERVER[mid] == 'T'){
                SWAP_SERVER(TAM_TAB_SERVER,low,mid);
                low++;
                mid++;
            }
            else if (TAM_TAB_SERVER[mid] == 'A'){
                mid++;
            }
            else if (TAM_TAB_SERVER[mid] == 'M'){
                SWAP_SERVER(TAM_TAB_SERVER,mid,high);
                high--;
            }
        }
        cout << "Here is the ordered sequence: " << TAM_TAB_SERVER << endl;
    }
}


