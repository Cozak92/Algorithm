#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
#define fs first;
#define se second;
#define PB push_back;
#define MP make_pair;
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

int room[MX][MX];
int n;
int ans = 0;

void bfs(){
    
    queue<pair<int,pii>> q;
    q.push(make_pair(0,make_pair(0,1)));

    while(!q.empty()){
    
        

        int x = q.front().second.first;
        int y = q.front().second.second;
        int dir = q.front().first;
        q.pop();
        if(x == n - 1 && y == n - 1){
            ans++;
            continue;
        }
        

        int nx = x + 1,ny = y + 1;
        if(dir == 0){ // 머리가 오른쪽

            if(ny < n && room[x][ny] != 1){ // 오른쪽 이동
                
                q.push(make_pair(0,make_pair(x,ny)));
            }
            if(nx < n && ny < n){ // 대각선 이동
                if(room[x][ny] != 1 && room[nx][ny] != 1 && room[nx][y] != 1){
                            
                    q.push(make_pair(1,make_pair(nx,ny)));
                }
            }
        }
        if(dir == 1){ //머리가 대각선
            if(ny < n && room[x][ny] != 1) // 오른쪽 이동
                q.push(make_pair(0,make_pair(x,ny)));
            if(nx < n && ny < n){ // 대각선 이동
                if(room[x][ny] != 1 && room[nx][ny] != 1 && room[nx][y] != 1){
                    q.push(make_pair(1,make_pair(nx,ny)));
                }
            }
            if(nx < n && room[nx][y] != 1) //야래로 이동
                q.push(make_pair(2,make_pair(nx,y)));

        }
        if(dir == 2){
             if(nx < n && room[nx][y] != 1) //야래로 이동
                q.push(make_pair(2,make_pair(nx,y)));
            if(nx < n && ny < n){ // 대각선 이동
                if(room[x][ny] != 1 && room[nx][ny] != 1 && room[nx][y] != 1){
                    q.push(make_pair(1,make_pair(nx,ny)));
                }
            }
        }
           
    }

}

void solve(){
    cin >> n;
    REP(i,n)
    REP(j,n) cin >> room[i][j];
    bfs();
    cout << ans << "\n";

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}