#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 20100;

int v,e,k;
int V,E;
struct Edge{
    int nextNode,dist;
};
// vector<pii> tree[MX];
vector<vector<Edge>> tree(MX);
int dist[MX];

void djik(int start){
    dist[start] = 0;
    priority_queue<pair<int,int>> pq;
    pq.push(make_pair(-dist[start],start));

    while (!pq.empty())
    {
       int curDist = -pq.top().first;
       int curNode = pq.top().second;
       pq.pop();

       if(curDist > dist[curNode]) continue;


       for(const auto edge : tree[curNode]){
           int nextNode = edge.nextNode;
           int nextDist = edge.dist;
           if(nextDist + curDist < dist[nextNode]){
               dist[nextNode] = nextDist + curDist;
               pq.push(make_pair(-dist[nextNode],nextNode));
           }
       }
    }
    
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> V >> E >> k;

    REP(i,E){
        int v,u,w;

        cin >> v >> u >> w;
        tree[v].push_back({u,w});
    }
    memset(dist,INF,sizeof(dist));
    djik(k);

    FOR(i,1,V+1){
        if(dist[i] == INF) cout << "INF" << "\n";
        else cout << dist[i] << "\n";
    }


}