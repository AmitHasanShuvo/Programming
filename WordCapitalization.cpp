//'''

Author : kazi_amit_hasan
Problem: Word Capitalization

Solution: Just change the 0th word to uppercase from lowercase and print with the rest.


#include<iostream>
using namespace std;
int main(){
    string s;
    cin>>s;
    s[0]=toupper(s[0]);
    cout<<s;
    return 0;
}