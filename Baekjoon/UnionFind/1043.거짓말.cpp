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
const int MX = 52;

int n,m,k;

int ans = 0;
int parent[MX];
vector<int> party[MX];
vector<int> truth;

int findParent(int a){
    if(parent[a] == a) return a;
    parent[a] = findParent(parent[a]);
    return findParent(parent[a]);
}

void doUnion(int a, int b){
    int A = findParent(a);
    int B = findParent(b);
    if(A< B) parent[B] = A;
    else parent[A] = B;
}

void solve(){
    cin >> n >> m;
    FOR(i,1,n+1) parent[i] = i;
    cin >> k;
    REP(i,k){
        int c; cin >> c;
        truth.push_back(c);
    }

    REP(i,m){
        int num; cin >> num;
        
        int prev;
        REP(j,num){
            int b; cin >> b;
            if(j == 0) prev = b;
            else doUnion(prev,b);
            party[i].push_back(b);
        }
        
    }
    int cnt =0; 
    for(auto list : party){
        what_is(++cnt);
        bool isPossible = 1;
        for(auto person : list){
            for(auto know : truth){
                if(findParent(person) == findParent(know)) {
                    isPossible = 0;
                }
            }
        }
        if(!isPossible) m--;
    }
    cout << m;



}



int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}