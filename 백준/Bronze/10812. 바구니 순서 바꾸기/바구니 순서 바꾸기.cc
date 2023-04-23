#include <vector>
#include <iostream>
using namespace std;
int main(){
    int N,M,s,e,p;
    cin>>N>>M;

    int arr[N+1]; 
    int tmpArr[N+1];
    for ( int i = 0 ; i < N+1 ; i++){
        arr[i] = i;
        tmpArr[i] = i;
    }

    // s p e 
    for (int i = 0; i < M; i++){
        cin>>s>>e>>p;
        for (int a = s; a < p; a++){
            tmpArr[a+e-p+1] = arr[a];
        }
        for (int j = p; j <= e; j++){
            tmpArr[j-p+s] = arr[j];
        }
        for (int c = s ; c <= e; c++){
            arr[c] = tmpArr[c];
        }
    }

    for (int i = 1; i < N+1; i++){
        cout<< arr[i] << " ";
    }

    return 0;
}