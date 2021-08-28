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
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0,   -1, -1, -1, 0, 1, 1, 1};
const int MX = 100000;


int sy[] = {-1,1,2};
int n,k;


void solve(){
    cin >> n >> k;
    if(n >= k){
        cout << n - k << "\n";
        cout << 1 << "\n";
        exit(0);
    }
    int waysCnt = 0;  
    int secCnt = INF;  
    queue<pii> q;
    q.push(make_pair(n,0));
    bool isVisited[MX+MX];


    while(!q.empty())
    {   int x = q.front().first;
        int curCnt = q.front().second;
        q.pop();

        isVisited[x] = true;
    
        if(x == k){
            if(curCnt < secCnt){
                secCnt = curCnt;
                waysCnt = 1;
            }
            else if(curCnt == secCnt){
                waysCnt++;
            }
            continue;
        }
    

    
        
        for(int i = 0; i < 3; i++){
            int nx;
            if(i == 2) nx = x * sy[i];
            else nx = x + sy[i];

            if(0 <= nx && nx <= MX) 
            if(!isVisited[nx]) q.push(make_pair(nx,curCnt + 1));
        }
    
    }
    cout << secCnt << "\n";
    cout << waysCnt << "\n";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}