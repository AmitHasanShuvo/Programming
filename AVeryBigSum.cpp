#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int num_of_elements;
    cin >> num_of_elements;
    vector<int> array(num_of_elements);
    long long int sum = 0;
    for (int i = 0; i < num_of_elements; i++)
    {
        cin >> array[i];
        sum += array[i];
    }
    cout << sum;
    return 0;
}
