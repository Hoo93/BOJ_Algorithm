#include <vector>
#include <iostream>
using namespace std;
int main(){
    int n,a,b,temp,m;
    cin>>n>>m;
    int *arr=new int[n];
    for (int i =0; i <n; i++){
        arr[i] = i+1;
    }
    for (int j = 0; j < m ; j++){
        cin>>a>>b;
        temp = arr[a-1];
        arr[a-1] = arr[b-1];
        arr[b-1] = temp;
    }

    for (int k = 0; k < n; k++){
        cout<<arr[k]<<" ";
    }
    return 0;
}