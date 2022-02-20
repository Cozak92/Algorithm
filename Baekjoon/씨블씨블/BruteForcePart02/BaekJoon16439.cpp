//
// Created by cozak on 2022-02-06.
//

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
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 10;
int N,M;
int people[31][31];
int answer = 0;
bool isVisited[31];
void dfs(vector<int> chicken){
    if(chicken.size() == 3){
        int sum = 0;
        REP(i,N) sum += max(max(people[i][chicken[0]], people[i][chicken[1]]), people[i][chicken[2]] );
        answer = max(answer,sum);
        return;
    }

    REP(i,M){
        if(isVisited[i]) continue;
        isVisited[i] = true;
        chicken.push_back(i);
        dfs(chicken);
        isVisited[i] = false;
        chicken.pop_back();
    }
}

void solve(){
    cin >> N >> M;

    REP(i,N){
        REP(j,M){
            cin >> people[i][j];
        }
    }
    vector<int> chicken;
    dfs(chicken);
    cout << answer;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}