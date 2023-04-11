#include <iostream>
#include <string>
using namespace std;

int main()
{

    int test_num;
    cin >> test_num;
    for (int i = 0; i < test_num; i++)
    {
        string str;
        cin >> str;
        cout << str[0] << str[str.length() - 1] << endl;
    }

    return 0;
}