//
// Created by cozak on 2022-02-21.
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

    queue<int> q;
    string input;
    int N;
    cin >> N;
    int X;
    REP (i, N) {
        cin >> input;
        if (input == "push") {
            cin >> X;
            q.push(X);
        } else if (input == "pop") {
            if (q.empty()) { cout << -1 << '\n'; }
            else {
                cout << q.front() << '\n';
                q.pop();
            }
        } else if (input == "size") { cout << q.size() << '\n'; }
        else if (input == "empty") {
            if (q.empty()) {
                cout << 1 << '\n';
            } else { cout << 0 << '\n'; }
        } else if (input == "front") {
            if (q.empty()) { cout << -1 << '\n'; }
            else {
                cout << q.front() << '\n';
            }
        } else if (input == "back") { if (q.empty()) { cout << -1 << '\n'; } else { cout << q.back() << '\n'; }}
    }


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}