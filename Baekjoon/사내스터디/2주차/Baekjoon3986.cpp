//
// Created by cozak on 2022-03-02.
//

#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define debug(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 10;



void solve(){
    int t;
    cin >> t;
    int count = 0;

    while(t--){
        string s;
        cin >> s;
        stack<char> stack;
        bool isGood = true;

        for(auto c: s){
            if(stack.empty()){
                stack.push(c);
            } else{
                if(stack.top() == c){
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        }
        if(!stack.empty()) isGood = false;
        if(isGood) count++;
    }
    cout << count;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}