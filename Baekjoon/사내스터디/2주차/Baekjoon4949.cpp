//
// Created by cozak on 2022-03-02.
//

#include <bits/stdc++.h>

using namespace std;
#define FOR(i, m, n) for(int i=(m);i<(n);i++)
#define REP(i, n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define debug(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int, int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 10;


void solve() {
    string ssss;

    while (1) {
        getline(cin, ssss);
        if (ssss.length() == 1 && ssss[0] == '.') break;

        stack<char> stk;
        bool flag = true;

        REP(i, ssss.length()) {
            if (ssss[i] == '(' || ssss[i] == '[') {
                stk.push(ssss[i]);
            }
            if (ssss[i] == ')') {
                if (stk.empty() || stk.top() != '(') {
                    flag = false;
                    break;
                } else {
                    stk.pop();
                }
            }
            if (ssss[i] == ']') {
                if (stk.empty() || stk.top() != '[') {
                    flag = false;
                    break;
                } else {
                    stk.pop();
                }
            }
        }
        if (stk.empty() && flag) cout << "yes" << "\n";
        else cout << "no" << "\n";
    }

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}