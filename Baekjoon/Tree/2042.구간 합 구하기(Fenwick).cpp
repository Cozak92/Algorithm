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
const int MX = 1000010;


ll arr[MX];
vector<ll> fenwick;
int n,m,k;

ll sumFenwick(int idx){
    ll sum = 0;
    while(idx > 0){
        sum += fenwick[idx];
        idx -= (idx & -idx);
    }
    return sum;
}

void update(int idx,ll diff){

    while(idx < fenwick.size()){
        // what_is(idx);
        fenwick[idx] += diff;
        // what_is(fenwick[idx]);
        idx += (idx & -idx);
    }
}

void solve(){
    cin >> n >> m >> k;
    fenwick = vector<ll> (n+1,0);
    FOR(i,1,n+1) cin >> arr[i], update(i,arr[i]);

    REP(i,m+k){
        ll a,b,c;
        cin >> a >> b >> c;
        if( a == 1){
            update(b,c - arr[b]);
            arr[b] = c;
        }

        else{
            cout << sumFenwick(c) - sumFenwick(b - 1) << "\n";
        }
    }

}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}