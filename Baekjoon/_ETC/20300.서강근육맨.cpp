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
const int MX = 100010;

int n;
vector<ll> arr;
ll ans;
void solve(){
  cin >> n;

  REP(i,n){
      ll a; cin >> a;
      arr.push_back(a);
  }
  sort(ALL(arr));

  if(n%2){
      ans = arr[n-1];
      REP(i,(n-1)/2){
          ans = max(ans,arr[i] + arr[n-2-i]);
      }
  }
  else {
		ans = arr[0] + arr[n - 1];
		REP(i,n/2)
			ans = max(ans, arr[i] + arr[n-1-i]);
	}
  cout << ans;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}