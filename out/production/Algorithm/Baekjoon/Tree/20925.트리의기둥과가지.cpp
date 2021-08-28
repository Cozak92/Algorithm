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
constexpr double DINF = 1.79769e+308;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 200010;

int n,r;
int g = 0;
ll dist[MX];
ll branchDist = 0;

vector<pii> tree[MX];
bool isVisited[MX];
bool isLeaf[MX];

void findGigaNode(int curNode){
    int cnt = 0;
    for(auto next : tree[curNode]){
        int nextNode = next.first;
        if(!isVisited[nextNode]){
            cnt++;
            if(cnt >= 2 && g == 0){
                g = curNode;
                break;
            }
            
        }
    }
    if(cnt == 0) isLeaf[curNode] = true;
    
    for(auto next : tree[curNode]){
        int nextNode = next.first;
        int nextDist = next.second;

        if(!isVisited[nextNode]){
            isVisited[nextNode] = true;
            dist[nextNode] = dist[curNode] + nextDist;
            findGigaNode(nextNode);
        }
    }
}

void solve(){
  cin >> n >> r;
  memset(dist,0,sizeof(dist));
  REP(i,n-1){
      int u,v,d;
      cin >> u >> v >> d;
      tree[u].push_back({v,d});
      tree[v].push_back({u,d});
  }
  isVisited[r] = true;
  findGigaNode(r);

  FOR(i,1,n+1){
      if(isLeaf[i]){
          branchDist = max(branchDist,dist[i] - dist[g]);
      }
  }
    if(g == 0) swap(branchDist,dist[g]);

  cout << dist[g] << " " << branchDist;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}