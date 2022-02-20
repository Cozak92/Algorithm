//
// Created by cozak on 2022-02-19.
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


int board[20][20];


void solve() {
    REP(i, 19) {
        REP(j, 19) {
            scanf("%d", &board[i][j]);
        }
    }

    REP(x, 19) {
        REP(y, 19) {
            if (board[x][y] != 0) {
                int finder = board[x][y];
                REP(k, 8) {
                    int cnt = 1;
                    int nx = x + dx8[k];
                    int ny = y + dy8[k];
                    int px = x - dx8[k];
                    int py = y - dy8[k];

                    if (0 <= px < 19 && 0 <= py < 19) {
                        if (board[px][py] == finder) {
                            continue;
                        }
                    }

                    while (0 <= nx < 19 && 0 <= ny < 19 && board[nx][ny] == finder) {
                        cnt++;
                        nx += dx[k];
                        ny += dy[k];
                    }

                    if (cnt == 5) {
                        cout << finder << endl;
                        cout << x + 1 << " " << y + 1;
                        return;
                    }
                }
            }
        }
    }

    cout << 0;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}