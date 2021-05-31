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
const int MX = 20;

struct bridge{
    int start,end,dist;

    friend bool operator <(const bridge& a, const bridge& b){
        return a.dist < b.dist;
    }
};

int n,m;
int parent[MX];
int board[MX][MX];
bool isVisited[MX][MX];
vector<bridge> bridges;

void makeLabel(int a,int b,int label){
    queue<pii> q;
    q.push(make_pair(a,b));
    board[a][b] = label;
    isVisited[a][b] = true;
 
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        REP(i,4){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] == 1){
                if(!isVisited[nx][ny]){
                    board[nx][ny] = label;
                    isVisited[nx][ny] = true;
                    q.push(make_pair(nx,ny));
                }
            }
        }
    }
}

void makeBridge(int a, int b, int label){
    REP(j,4){
        int nx = a;
        int ny = b;
        int dist = 0;
        bridge temp;
        while(1){
            nx += dx[j];
            ny += dy[j];
            // what_is(nx);
            // what_is(ny);
            if(0 <= nx && nx < n && 0 <= ny && ny < m){
                if(board[nx][ny] == 0){
                    dist++;
                }
                else if(board[nx][ny] != label){
                    if(dist > 1){
                        temp.start = label;
                        temp.end = board[nx][ny];
                        temp.dist = dist;
                        // what_is(temp.start);
                        // what_is(temp.end);
                        // what_is(temp.dist);
                        bridges.push_back(temp);
                        break;

                    }
                    else break;//길이 1이하
                }
                else break; // 같은 라벨
            }
            else break; // 범위 벗어남
            
        }
    }
  
}

int find(int x){
    if(parent[x] == x) return x;
    parent[x] = find(parent[x]);

    return find(parent[x]);

}

void doUnion(int a, int b){
    int rootA = find(a);
    int rootB = find(b);

    if(rootA < rootB){
        parent[rootB] = rootA;
    }
    else{
        parent[rootA] = rootB;
    }
}

void solve(){

    cin >> n >> m;
    REP(i,n)
    REP(j,m) cin >> board[i][j];
    int label = 1;

    REP(i,n)
    REP(j,m){
        if(!isVisited[i][j] && board[i][j] == 1){
            makeLabel(i,j,label);
            label++;
        }
    }
    // REP(i,n){ //라벨확인
    //     cout << "---------";
    //     REP(j,m) cout << board[i][j] << " ";
    //     cout << "\n";
    // }
    REP(i,n){
        REP(j,m){
            if(board[i][j]){
                makeBridge(i,j,board[i][j]);
            }
        }
    }
    int ans = 0;
    REP(i,MX+1) parent[i] = i;
    sort(ALL(bridges));

    for(auto bridge : bridges){
        int a = bridge.start;
        int b = bridge.end;
        if(find(a) != find(b)){
            ans += bridge.dist;
            doUnion(a,b);
        }
    }

    int current = find(1);

    FOR(i,2,label){
        if(current != find(i)){
            cout << -1;
            return;
        }
    }

    cout << ans;
    
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}
