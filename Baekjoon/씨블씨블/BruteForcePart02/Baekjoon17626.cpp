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


void solve() {
    int n;

    cin >> n;
    int answer = 0;
    int counter = 0;
    while (answer != n) {
        REP(i, 225) {
            int temp = pow(i, 2);

            if (answer + temp > n) {
                cout << " i = " << i << endl;
                cout <<  pow(i - 1, 2) << endl;
                answer += pow(i - 1, 2);
                counter++;
                break;
            }
        }
    }

    cout << counter;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}