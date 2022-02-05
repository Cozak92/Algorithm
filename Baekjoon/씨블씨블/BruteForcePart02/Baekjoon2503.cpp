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
int n;
bool arr[1000];

void solve() {
    memset(arr, true, 1000);
    cin >> n;
    REP(i, n) {
        int s, b;
        string num;
        cin >> num >> s >> b;
        FOR(j, 123, 988) {
            int ss = 0, bb = 0;
            string num2 = to_string(j);
            unordered_set<char> se;
            REP(k, num2.length()) {
                se.insert(num2[k]);
            }
            if (se.size() != 3) {
                arr[j] = false;
                continue;
            }

            if (se.find('0') != se.end()) {
                arr[j] = false;
                continue;
            }

            REP(k, 3) {
                REP (l, 3) {
                    if (k == l && num[k] == num2[l]) {
                        ss++;
                        continue;
                    }
                    if (num[k] == num2[l]) {
                        bb++;
                    }
                }
            }
            if (ss != s || bb != b) {
                arr[j] = false;
            }
        }
    }
    int answer = 0;
    FOR(i,123, 988) {
        if (arr[i]) {
            answer++;
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