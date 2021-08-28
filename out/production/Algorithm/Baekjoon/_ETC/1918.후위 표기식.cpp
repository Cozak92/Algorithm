#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 1;

void solve(){
    string s;
    cin >> s;
    vector<char> stk;
    for(auto c: s){
        if(isalpha(c)) cout << c;
        else{
            if(c == '(') stk.push_back(c);
            if(c == '+' || c == '-'){
                while(!stk.empty() && stk.back() != '('){
                    cout << stk.back();
                    stk.pop_back();
                }
                stk.push_back(c);
            }
            if(c == '*' || c == '/'){
                while(!stk.empty() && (stk.back() == '*' || stk.back() == '/')){
                    cout << stk.back();
                    stk.pop_back();
                }
                stk.push_back(c);
            }
            if(c == ')'){
                while(!stk.empty() && stk.back() != '('){
                    cout << stk.back();
                    stk.pop_back();
                }
                stk.pop_back();
            }
        }
    }
    while(!stk.empty()){
        cout << stk.back();
        stk.pop_back();
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}