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
const int MX = 42;

unordered_map<int,int> counter;
int arr[MX];
ll ans = 0;
int n,s,half;

void dfsLeft(int idx, int sum){
	if(idx == half){
		counter[sum]++; return;
	}
	dfsLeft(idx+1, sum);
	dfsLeft(idx+1, sum + arr[idx]);
}

void dfsRight(int idx, int sum){
	if(idx == n){
		ans += counter[s-sum]; return;
	}
	dfsRight(idx+1, sum);
	dfsRight(idx+1, sum + arr[idx]);
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n >> s;
	half = n/2;
	REP(i,n) cin >> arr[i];
	dfsLeft(0, 0);
	dfsRight(half, 0);
	if(s == 0) ans--;
	cout << ans;
}