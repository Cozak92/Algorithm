#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 50010;
int n,m;
int LOG = 19;
int parent[MX];
bool isVisited[MX];
vector<int> tree[MX];
vector<vector<int>> query;
vector<int> depth;
vector<vector<int>> up;

void findParent(int curNode){
    if(curNode > n) return;

    for(int nextNode : tree[curNode]){
        if(!isVisited[nextNode]){
            // parent[nextNode] = curNode;
            depth[nextNode] = depth[curNode] + 1;
            up[nextNode][0] = curNode;
            isVisited[nextNode] = true;
            findParent(nextNode);
        }
    }

}

void make(){
    parent[1] = 1;
    FOR(j,1,LOG){
        FOR(v,1,n+1){
            up[v][j] = up[ up[v][j - 1] ][j - 1]; //sparse
        }
    }
}

int getLCA(int a, int b){

    if(depth[a] < depth[b]) swap(a,b);

    int diff = depth[a] - depth[b];
    for(int i = LOG - 1; i >= 0; i--){
        if(diff & (1 << i)){
            a = up[a][i];
        }
    }

    if(a == b) return a;

    for(int j = LOG - 1; j >= 0; j--){
        if(up[a][j] != up[b][j]){
            a = up[a][j];
            b = up[b][j];
        }
    }

    return up[a][0];

}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    int node1,node2;
    // tree = vector<vector<int>>(n,vector<int>(n));
    REP(i,n-1){
        cin >> node1 >> node2;
        tree[node1].push_back(node2);
        tree[node2].push_back(node1);
    }
    isVisited[1] = true;
    up = vector<vector<int>>(n + 1,vector<int>(LOG));
    depth = vector<int>(n + 1);
    findParent(1);

    while ((1 << LOG) <= n){
        LOG++;
    }

    make();

    cin >> m;
    REP(i,m){
        int a,b;
        cin >> a >> b;
        cout << getLCA(a,b) << "\n";
    }

    // for(int ans: answer) cout << ans << "\n";

    
}