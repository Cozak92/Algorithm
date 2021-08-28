#include <iostream>

using namespace std;

int t;
int k ;
double e,w;
int ans;

// k%의 매직에센스를 가지고있따

// 스텝별로 1리터의 매직에센서를 넣던가 1리터의 물을 넣는다.
int gcd(int a, int b){
    int c;
    while(b !=0){
        c = a % b;
        a = b;
        b = c;
    }

    return a;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> t;

    while(t--){
        ans = 0;
        cin >> k;
        int x = 100 - k;
        int y = k;
        int q = gcd(x,y);

        if(q){
            ans += x / q;
            ans += y / q;
            cout << ans <<"\n";
        }
        else{
            cout << 100 << "\n";
        }
        

    }
}