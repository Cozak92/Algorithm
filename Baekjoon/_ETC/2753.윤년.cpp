#include <iostream>
using namespace std;
int year;


int64_t solve(){

    if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0){
        return 1;
    }
    return 0;
}

int main(){
    cin >> year;

    cout << solve();
}