#include <vector>
#include <iostream>
using namespace std;
int main(){
    int N,M,a,b,tmp;
    cin>>N>>M;
    int *arr =  new int[N+1];
    for (int i = 0 ; i < N+1 ; i++){
        arr[i] = i;
    }
    for (int i = 0 ; i < M ; i++){
        cin>>a>>b;
        for (int j = 0 ; j < (b-a+1)/2 ; j++){
            tmp = arr[b-j];
            arr[b-j] = arr[a+j];
            arr[a+j] = tmp;
        }
    }

    for (int k = 1; k < N+1 ; k++){
        cout<<arr[k]<<" ";
    }
    return 0;
}