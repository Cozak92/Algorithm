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
const int MX = 100010;

int n,m;
int arr[MX];
int LOG;
vector<ll> tree;

ll init(int left, int right, int node){
  if(left == right) return tree[node] = arr[left];
  ll mid = left + (right - left) / 2;
  return tree[node] = min(init(left,mid,(node << 1)), init(mid + 1,right,(node << 1) + 1));
}

ll findMin(int left,int right, int node, int start, int end){
  if(left > end || right < start) return LINF;
  if(start <= left && right <= end) return tree[node];
  ll mid = left + (right - left) / 2;
  return min(findMin(left,mid,(node << 1), start, end), findMin(mid + 1, right,( node << 1) +1, start, end));
}



void solve(){
  cin >> n >> m;
  
  FOR(i,1,n+1) cin >> arr[i];
  while((1 << LOG) <= n) LOG++;
  LOG++;
  tree = vector<ll> ((1 << LOG));

  init(1,n,1);

  REP(i,m){
    int a,b; cin >> a >> b;
    cout << findMin(1,n,1,a,b) << '\n';
  }

}


int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  solve();
}