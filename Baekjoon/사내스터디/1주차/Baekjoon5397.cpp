//
// Created by cozak on 2022-02-20.
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


    while(t--){
        vector<char> stack1;
        vector<char> stack2;

        string input;
        cin >> input;

        for(auto s: input){
            if( s == '<' && !stack1.empty()){
                stack2.push_back(stack1.back());
                stack1.pop_back();
            }
           if( s == '>' && !stack2.empty()){
                stack1.push_back(stack2.back());
                stack2.pop_back();
            }
            if( s == '-' && !stack1.empty()){
                stack1.pop_back();
            }
            if( isalnum(s)){
                stack1.push_back(s);
            }
        }

        while(!stack2.empty()){
            stack1.push_back(stack2.back());
            stack2.pop_back();
        }

        REP(i,stack1.size()){
            cout << stack1[i];
        }
        cout << "\n";

    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}
