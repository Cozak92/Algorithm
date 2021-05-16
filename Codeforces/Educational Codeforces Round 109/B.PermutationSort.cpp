#include <bits/stdc++.h>

using namespace std;

int t;
int n,m;
int arr[100];


void solve(){
    cin >> t;

    while(t--){
        cin >> n;
        bool isSorted = true;
        for(int i =1; i<=n; i ++){
            cin >> arr[i];
            if(arr[i] != i) isSorted = false;
        }
        //아이디어 = 배열 원소의 앞 뒤만 보고 몇번 섞어야하는지 확인한다.
        if(isSorted) cout << 0;
        else if(arr[1] == 1 || arr[n] == n) cout << 1;
        else if(arr[1] == n && arr[n] == 1) cout << 3;
        else cout << 2;
        cout << "\n";
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    

    solve();

}