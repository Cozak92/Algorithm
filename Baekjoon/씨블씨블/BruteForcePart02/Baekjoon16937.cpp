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
int h, w;


bool isPossible(int w1, int h1, int w2, int h2) {
    if (h1 + h2 <= h && max(w1, w2) <= w) return true;
    if (max(h1, h2) <= h && w1 + w2 <= w) return true;
    return false;
};

bool canRotate(int w1, int h1, int w2, int h2){
    if (isPossible(w1, h1, w2, h2)) return true;
    if (isPossible(h1, w1, w2, h2)) return true;
    if (isPossible(w1, h1, h2, w2)) return true;
    if (isPossible(h1, w1, h2, w2)) return true;
    return false;
}

void solve() {
    cin >> h >> w;
    int n;
    cin >> n;
    int width[n], height[n];
    int answer = 0;
    REP(i, n) {
        cin >> width[i] >> height[i];
    }
    REP(i, n) {
        FOR(j, i + 1, n) {
            int w1 = width[i], h1 = height[i];
            int w2 = width[j], h2 = height[j];
            if(!canRotate(w1,h1,w2,h2)) continue;
            answer = max(answer, (w1 * h1 + w2 * h2));
        }
    }
    cout << answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}