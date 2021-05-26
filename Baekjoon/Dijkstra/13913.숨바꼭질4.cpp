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
const int MX = 100000;

priority_queue<pii> q;
int n,k;
int sy[] = {-1,1,2};
int tracking[MX + MX];

void solve(){
    cin >> n >> k;

    int minSec = INF;
    int dist[MX+ MX];
    fill(dist,dist+MX+MX,INF);



    if(n >= k){
        cout << n - k << "\n";
        for(int i = n; i >= k; i--){
            cout << i << " ";
        }
        exit(0);
    }
    dist[n] = 0;
    q.push(make_pair(-dist[n],n));

    while(!q.empty()){

        int x = q.top().second;
        int curSec = -q.top().first;
        
        q.pop();
    
        if(curSec > dist[x]) continue;
        // what_is(x);
        REP(i,3){
            int nx,nextSec;
            if(i == 2){
                nx = x * sy[i];
                nextSec = curSec + 1;
            }
            else{
                nx = x + sy[i];
                nextSec = curSec + 1;
            }
    
            if(0 <= nx && nx <= MX + MX){
                if(nextSec < dist[nx]){
                    dist[nx] = nextSec;
                    q.push(make_pair(-dist[nx],nx));
                    tracking[nx] = x;
                }
            }
        }
    }
    cout << dist[k] << "\n";
    vector<int> ans;
    ans.push_back(k);
    for(;k != n; k = tracking[k]) ans.push_back(tracking[k]);

    reverse(ALL(ans));

    for(auto e: ans) cout << e << " ";
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}