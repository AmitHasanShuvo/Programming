#include <bits/stdc++.h>
#include<assert.h>

using namespace std;

void solution() {

     int n, x;

     cin >> n;

     assert(n > 0 && n <= 60);

     for(int i = 0; i < n; i++)
     {
        cin >> x;
        assert(x >= 0 && x <= 100);
        if(x >= 38)
        {
            int y = x;
            while(1)
            {
               if(y % 5 == 0)
				break;
               y++;
            }
            if(y - x <= 2)
             x = y;
        }
        cout << x << endl;
     }
}

int main () {
    
        solution();

    return 0;
}