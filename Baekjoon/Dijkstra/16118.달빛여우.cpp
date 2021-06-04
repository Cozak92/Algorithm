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
const int MX = 4010;

int n,m;

vector<pair<int,ll>> tree[MX];
ll wolfDist[MX][2];
ll foxDist[MX];

struct Fox{
  int x;
  ll dist;
};
struct Wolf{
  int x;
  ll dist;
  int rest;
};

struct foxComp{
  bool operator()(const Fox& a, const Fox& b){
    return a.dist > b.dist;
  }
};

struct wolfComp{
  bool operator()(const Wolf& a, const Wolf& b){
    return a.dist > b.dist;

  }
};

void foxDjik(){

  REP(i,n+1){
    foxDist[i] = LINF;
    foxDist[i] = LINF;
  }
  priority_queue<Fox,vector<Fox>,foxComp> pq;
  Fox temp;

  foxDist[1] = 0;
  temp.x = 1;
  temp.dist = foxDist[1];
  pq.push(temp);

  while(!pq.empty()){
    int curNode = pq.top().x;
    ll curdist = pq.top().dist;
    pq.pop();
    if(curdist > foxDist[curNode]) continue;
    
    for(auto next : tree[curNode]){
      int nextNode = next.first;
      ll nextDist = next.second;
      if(foxDist[nextNode] > nextDist + curdist){
        foxDist[nextNode] = nextDist + curdist;
        temp.x = nextNode;
        temp.dist = foxDist[nextNode];
        pq.push(temp);
      }


    }
    

  }
}

void wolfDjik(){
  REP(i,n+1){
    wolfDist[i][0] = LINF;
    wolfDist[i][1] = LINF;
  }
  priority_queue<Wolf,vector<Wolf>,wolfComp> pq;
  Wolf wolf;

  wolfDist[1][0] = 0;
  wolf.x = 1;
  wolf.dist = wolfDist[1][0];
  wolf.rest = 0;
  pq.push(wolf);

  while(!pq.empty()){
    int curNode = pq.top().x;
    ll curDist = pq.top().dist;
    int curRest = pq.top().rest;
    pq.pop();
    if(curDist > wolfDist[curNode][curRest] ) continue;

    for(auto next: tree[curNode]){
      ll nextDist;
  
      if(curRest) nextDist = (ll)next.second * 2;
      else nextDist = (ll)next.second / 2;

      int nextNode = next.first;
      
      int temp;
      if(curRest) temp =0;
      else temp = 1;
      
      if(wolfDist[nextNode][temp] > nextDist + curDist){

        wolfDist[nextNode][temp] = nextDist + curDist;
        wolf.x = nextNode;
        wolf.dist = wolfDist[nextNode][temp];
        wolf.rest = temp;
        pq.push(wolf);
      }
    }
    
  }
  
}

void solve(){
  cin >> n >> m;
  REP(i,m){
    int v,u,d;
    cin >> v >> u >> d;
    tree[v].push_back({u,d * 2});
    tree[u].push_back({v,d * 2});
  }

  wolfDjik();
  foxDjik();
  int ans = 0;
  FOR(i,2,n+1){
    // debug(i);
    // debug(foxDist[i]);
    // debug(wolfDist[i][0]);
    // debug(wolfDist[i][1]);
    if(foxDist[i] < wolfDist[i][0] && foxDist[i] < wolfDist[i][1]){
      ans++;
    }
  }
  cout << ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}