#include<bits/stdc++.h>
using namespace std;
int main(){
    int num_of_elements;
    cin>>num_of_elements;
    vector <int> array(num_of_elements);
    int sum = 0;
    for (i=0;i<num_of_elements;i++){
        cin>>array[i];
        sum +=array[i];
    }
    cout<<sum;
    return 0;
}
