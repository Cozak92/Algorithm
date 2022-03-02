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

    int N, M, ans;
    deque<int> deq;

    cin >> N >> M;
    FOR(i, 1, N + 1) {
        deq.push_back(i);
    }
    ans = 0;
    while (M--) {
        int a,index;
        cin >> a;

        REP(i,deq.size()){
            if(deq[i] == a) index = i;
        }

        if( deq.size() / 2 >= index){
            REP(j,index){
                deq.push_back(deq.front());
                deq.pop_front();
                ans++;
            }
            deq.pop_front();
        }
        else {
            REP(j,deq.size()-index){
                deq.push_front(deq.back());
                deq.pop_back();
                ans++;
            }
            deq.pop_front();
        }
    }
    cout << ans << endl;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}