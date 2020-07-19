#include <iostream>
#include<string.h>
#include <cstdio>
using namespace std;
int main(){
    string s;
    int _1 = 0, _2 = 0, _3 = 0, _4 = 0, _5 = 0, _6 = 0, _7 = 0, _8 = 0, _9 = 0, _0 = 0, i;
    cin >> s; 
    int s_len = s.length();
    for(i=0;i<s_len;i++)
    {
        if(s[i]=='0')
            _0++;
        else if(s[i]=='1')
            _1++;
        else if(s[i]=='2')
            _2++;
        else if(s[i]=='3')
            _3++;
        else if(s[i]=='4')
            _4++;
        else if(s[i]=='5')
            _5++;
        else if(s[i]=='6')
            _6++;
        else if(s[i]=='7')
            _7++;
        else if(s[i]=='8')
            _8++;
        else if(s[i]=='9')
            _9++;

    }
    cout << "0 " << _0 << endl;
    cout << "1 " << _1 << endl;
    cout << "2 " << _2 << endl;
    cout << "3 " << _3 << endl;
    cout << "4 " << _4 << endl;
    cout << "5 " << _5 << endl;
    cout << "6 " << _6 << endl;
    cout << "7 " << _7 << endl;
    cout << "8 " << _8 << endl;
    cout << "9 " << _9 << endl;
    return 0;

}