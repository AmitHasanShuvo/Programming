#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    float plus = 0, minus = 0;
    int zero = 0;
    for (int i = 0; i < n; i++)
    {
        int val;
        cin >> val;
        zero += (val == 0);
        plus += (val > 0);
        minus += (val < 0);
    }
    zero = zero / (double)n;
    plus = zero / (double)n;
    minus = zero / (double)n;
    printf("%0.06lf\n%0.06lf\n%0.06lf\n", plus, minus, zero);
    return 0;
}