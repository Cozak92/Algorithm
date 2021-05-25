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

int n,m,k;
int LOG = 0;
ll arr[MX];
ll a,b,c;
vector<ll> tree;

ll initSegtree(int left, int right, int node){
    if(left == right) return tree[node] = arr[left];
    ll mid = left + (right - left) / 2;
    return tree[node] = initSegtree(left,mid,node * 2) +  initSegtree(mid + 1, right,node * 2 + 1);
}

void updateSegtree(int left, int right,int node,ll diff,int idx){
    if(left > idx || right < idx) return;
    tree[node] += diff;
    if(left != right){
        ll mid = left + (right - left) / 2;
        updateSegtree(left,mid,node * 2,diff, idx);
        updateSegtree(mid + 1, right,node * 2 + 1, diff, idx);
    }
}

ll SumSegtree( int left, int right,int node, int start, int end){

    if(left > end || right < start) return 0;
    if(start <= left && right <= end){return tree[node];} 
    ll mid = left + (right - left) / 2;
    return SumSegtree(left, mid,node * 2, start,end) + SumSegtree(mid + 1, right ,node * 2 + 1,start,end);
}

void solve(){
    cin >> n >> m >> k;
    while((1 << LOG) <=n){
        LOG++;
    }
    LOG++;
    tree = vector<ll> ((1<<LOG));
    FOR(i,1,n+1) cin >> arr[i];
    initSegtree(1,n,1);

    

    REP(i,m+k){
       int order;
        cin >> order >> b >> c;
        if(order == 1){
            
            updateSegtree(1,n,1,c - arr[b],b);
            arr[b] = c;

            // REP(i,(1<<LOG)+2) what_is(tree[i]), what_is(i);
        }
        else{
            cout << SumSegtree(1,n,1,b,c) << "\n";
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}