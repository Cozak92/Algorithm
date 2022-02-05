//
// Created by cozak on 2022-02-05.
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
int N, K;
int counter = 0;
int arr[5];
int answer = -1;

void dfs(int cur, int step) {

    if (step > counter)return;
    if (cur > N) return;

    answer = max(answer, cur);

    REP(i, K) {
        dfs(cur * 10 + arr[i], step + 1);
    }
}

void solve() {
    cin >> N >> K;
    REP(i, K) {
        cin >> arr[i];
    }
    int T = N;
    while (T) {
        T /= 10;
        counter++;
    }


    dfs(0,0);

    cout << answer;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}