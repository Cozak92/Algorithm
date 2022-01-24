//
// Created by cozak on 2022-01-24.
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
int A, B, C, M;


void solve() {
    cin >> A >> B >> C >> M;
    int workHours = 0;
    int curFatigue = 0;
    REP(i,24) {
        if (curFatigue + A <= M) {
            curFatigue += A;
            workHours++;
        } else {
            curFatigue -= C;
            curFatigue = curFatigue <= 0 ? 0 : curFatigue;
        }
    }

    cout << workHours * B;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();


}