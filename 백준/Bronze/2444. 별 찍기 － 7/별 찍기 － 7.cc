#include <vector>
#include <iostream>
using namespace std;
int main(){
    int N;
    string tmp;
    cin>>N;
    for (int i = 0 ; i < N-1 ; i++){
        for (int j = (N-i-1) ; j > 0; j-- ){
            cout << " ";    
        }
        for (int k = 0; k < 2*i+1 ; k++){
            cout << "*";
        }
        cout << endl;
    }
    for (int i = 0 ; i < 2*N-1 ; i++){
        cout << "*";
    }
    cout << endl;
    for (int i = 0 ; i < N-1 ; i++){
        for (int j = 0 ; j <= i ; j++ ){
            cout << " ";    
        }
        for (int k = 2*(N-i-1)-1; k > 0 ; k--){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}