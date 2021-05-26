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
const int MX = 100100;

int n,q;

ll tree[2 * MX];
void init(){
    for(int i = n - 1; i > 0; i--) tree[i] = tree[i << 1] + tree[i << 1|1];
}

void modify(int p, int val){    
    for(tree[p+=n] = val; p > 1; p >>= 1) tree[p>>1] = tree[p] + tree[p^1];
} 

ll query(int left, int right){
    ll res = 0;
    for(left += n, right += n; left < right; left >>= 1, right >>=1){
        if(left&1) res += tree[left++];
        if(right&1) res += tree[--right];
    }
    return res;
}

void solve(){
    cin >> n >> q;
    FOR(i,n,2 * n) cin >> tree[i];
    
    init();
    int x,y,a,b;
    REP(i,q){
        cin >> x >> y >> a >> b;
        if( x > y) swap(x,y);
        
        cout << query(x- 1,y) << "\n";
        modify(a - 1,b);
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}