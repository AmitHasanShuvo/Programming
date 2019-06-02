#include <bits/stdc++.h>
using namespace std;
int main()
{

    vector<int> a(3);
    vector<int> b(3);
    int alice = 0;
    int bob = 0;

    for (int i = 0; i < 3; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < 3; i++)
    {
        cin >> b[i];
    }
    for (int i = 0; i < 3; i++)
    {
        if (a[i] > b[i])
            alice++;
        if (a[i] < b[i])
            bob++;
    }
    cout << alice << " " << bob << endl;
    return 0;
}