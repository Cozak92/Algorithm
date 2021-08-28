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
const int MX = 25;
int n,m;
ll fuel;
int board[MX][MX];
pii taxi;
struct guest{
    int startX,startY;
    int destX,destY;
    int dist;
    bool done;

    friend bool operator < (const guest& a, const guest& b){
        if(a.dist < b.dist) return true;
        if(a.dist > b.dist) return false;
        if(a.startX < b.startX) return true;
        if(a.startX > b.startX) return false;
        if(a.startY < b.startY) return true;
        return false;
    }
}guests[500];
bool isComplete[500];

int bfs(int a, int b, int xx, int yy){
    queue<pair<int,pii>> q;
    bool isVisited[MX][MX];
    memset(isVisited,false,sizeof(isVisited));
    q.push(make_pair(0,make_pair(a,b)));
    isVisited[a][b] = true;
    int ret = INF;

    while(!q.empty()){
        int x = q.front().second.first;
        int y = q.front().second.second;
        int dist = q.front().first;

        q.pop();
        if( x == xx && y == yy){
            ret = min(dist,ret);
            continue;
        } 
        

        REP(k,4){
            int nx = x + dx[k];
            int ny = y + dy[k];
            if(0 < nx && nx <= n && 0 < ny && ny <= n && board[nx][ny] != 1){
                if(!isVisited[nx][ny]){
                    isVisited[nx][ny] = true;
                    q.push(make_pair(dist+1,make_pair(nx,ny)));
                }
            }
        }
    }
    return ret;
}

void solve(){
    cin >> n >> m >> fuel;

    FOR(i,1,n+1)
    FOR(j,1,n+1){
        cin >> board[i][j];
    }

    int a,b;
    cin >> a >> b;
    taxi = make_pair(a,b);
    REP(i,m){
        cin >> guests[i].startX >> guests[i].startY >> guests[i].destX >> guests[i].destY;
    }
    REP(j,m){

        REP(i,m){
            if(!guests[i].done){
                // debug(guests[i].startX);
                // debug(guests[i].startY);
                guests[i].dist = bfs(taxi.first,taxi.second,guests[i].startX,guests[i].startY);
                // debug(guests[i].dist);
            }
        }
        
        sort(guests,guests+m);

        REP(i,m){
            if(!guests[i].done){
                if( guests[i].dist > fuel){
                    cout << -1;
                    return;
                }
                fuel -= guests[i].dist;
                int temp = bfs(guests[i].startX,guests[i].startY,guests[i].destX,guests[i].destY);
                if(temp > fuel){
                    cout << -1;
                    return;
                }
                guests[i].done = true;
                fuel += temp;

                taxi.first = guests[i].destX;
                taxi.second = guests[i].destY;
                break;
            }
        }


    }

    cout << fuel;


  
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}