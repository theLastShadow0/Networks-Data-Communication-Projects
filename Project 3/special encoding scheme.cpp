#include <iostream>

using namespace std;

int main(){
    //Setting -121 as the starting point 0 [-1,-1,-1,-1,-1]
    int x0 = -1;
    int x1 = -1;
    int x2 = -1;
    int x3 = -1;
    int x4 = -1;
    int counter = 0;
    int N;

    cout << "Please input a number between -121 and 121:" << endl;
    cin >> N;

    for (int i = 0; i < 121 + N; i++){
        counter++;

        //For 3^0 cycles every iteration
        if (counter % 1 == 0){
            if (x0 == -1){
                x0 = 0;
            }
            else if (x0 == 0){
                x0 = 1;
            }
            else if (x0 == 1){
                x0 = -1;
            }
        }
        //For 3^1 cycles every 3 iterations
        if (counter % 3 == 0){
            if (x1 == -1){
                x1 = 0;
            }
            else if (x1 == 0){
                x1 = 1;
            }
            else if (x1 == 1){
                x1 = -1;
            }
        }
        //For 3^2 cycles every 9 iterations
        if (counter % 9 == 0){
            if (x2 == -1){
                x2 = 0;
            }
            else if (x2 == 0){
                x2 = 1;
            }
            else if (x2 == 1){
                x2 = -1;
            }
        }
        //For 3^3 cycles every 27 iterations
        if (counter % 27 == 0){
            if (x3 == -1){
                x3 = 0;
            }
            else if (x3 == 0){
                x3 = 1;
            }
            else if (x3 == 1){
                x3 = -1;
            }
        }
        //For 3^4 cycles every 81 iterations
        if (counter % 81 == 0){
            if (x4 == -1){
                x4 = 0;
            }
            else if (x4 == 0){
                x4 = 1;
            }
            else if (x4 == 1){
                x4 = -1;
            }
        }
    }
    cout << N << " is: " <<"[" << x4 << ", " << x3 << ", " << x2 << ", " << x1 << ", " << x0 << "]" << endl;

    return 0;
}
