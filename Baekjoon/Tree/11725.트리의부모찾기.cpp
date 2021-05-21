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
const int MX = 100010;

vector<int> tree[MX];
bool isVisited[MX];
int parents[MX];
int n;

void dfs(int curNode){
    if(curNode > n){
        return;
    }

    for(int nextNode : tree[curNode]){
        // int nextNode = tree[curNode][i];
        if(!isVisited[nextNode]){
            parents[nextNode] = curNode;
            isVisited[nextNode] = true;
            dfs(nextNode);
        }
    }

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    REP(i,n-1){
        int node1, node2;

        cin >> node1 >> node2;

        tree[node1].push_back(node2);
        tree[node2].push_back(node1);
    }
    isVisited[1] = true;
    dfs(1);

    FOR(i,2,n+1){
        cout << parents[i] << "\n";
    }
    
}