#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define debug(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 10010;

int n,ans,c;
int dist[MX];
vector<pii> tree[MX];

void dfs(int curNode,int len){
    if(dist[curNode] != -1) return;
    // debug(curNode);
    dist[curNode] = len;

    if(ans < dist[curNode]){
        ans = dist[curNode];
        c = curNode;
    }

    for(auto e : tree[curNode]){
        int nextNode = e.first;
        int weight = e.second;
        dfs(nextNode, len + weight);

    }

}

void solve(){
  cin >> n;
    ans = 0;
  REP(i,n-1){
    int v,u,w;
    cin >> v >> u >> w;
    tree[v].push_back({u,w});
    tree[u].push_back({v,w});
  }
    memset(dist,-1,sizeof(dist));
  dfs(1,0);
  memset(dist,-1,sizeof(dist));
  dfs(c,0);

  cout << ans;


}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}
