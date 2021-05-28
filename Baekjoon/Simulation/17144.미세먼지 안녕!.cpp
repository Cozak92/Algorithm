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

int room[MX][MX];
int r,c,t;
vector<pii> air;
queue<pii> q;

void spread(){
    int spreads[MX][MX];
    memset(spreads,0,sizeof(spreads));
    while(!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        int t = room[x][y] / 5;
            REP(k,4){
                int nx = x + dx[k];
                int ny = y + dy[k];
                if( 0 <= nx && nx < r && 0 <= ny && ny < c && room[nx][ny] != -1){
                    spreads[nx][ny] += t;
                    spreads[x][y] -= t;
                }
            }

    }
    REP(x,r)
    REP(y,c){
        room[x][y] += spreads[x][y];
    }
    // cout << "--------확산---------\n";
    // REP(i,r){
    //     REP(j,c){
    //         cout << room[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

}

void doAir(){
    //up

    int fx = air[0].first;
    int fy = air[0].second;
    int sx = air[1].first;
    int sy = air[1].second;

    for(int x = fx; x > 0; x--){ // |
        if(x == fx) room[x - 1][fy] = 0; 
        else room[x][fy] = room[x - 1][fy];
    }
    // ㅡ
    for(int y = fy; y < c - 1; y++) room[0][y] = room[0][y + 1];
    // |
    for(int x = 0; x < fx; x++) room[x][c - 1] = room[x + 1][c - 1];
    // ㅡ
    for(int y = c - 1; y > fy + 1; y--) room[fx][y] = room[fx][y - 1];
    room[fx][fy + 1] = 0;

    // cout << "--------위---------\n";
    // REP(i,r){
    //     REP(j,c){
    //         cout << room[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    // down

    for(int x = sx; x < r; x++){
        if(x == sx) room[x + 1][sy] = 0;
        else room[x][sy] = room[x + 1][sy];
    }
    for(int y = 0; y < c - 1; y++) room[r - 1][y] = room[r - 1][y + 1];
    for(int x = r - 1; x > fx; x--) room[x][c - 1] = room[x - 1][c - 1];
    for(int y = c - 1; y > sy + 1; y--) room[sx][y] = room[sx][y - 1];
    room[sx][sy + 1] = 0;
    // cout << "--------아래---------\n";
    // REP(i,r){
    //     REP(j,c){
    //         cout << room[i][j] << " ";
    //     }
    //     cout << "\n";
    // }

    
}

void solve(){

    cin >> r >> c >> t;

    REP(i,r)
    REP(j,c) {
        cin >> room[i][j];
        if(room[i][j] == -1) air.push_back(make_pair(i,j));
    }


    while(t--){
        REP(x,r)
        REP(y,c){
            if(room[x][y] != -1 && room[x][y] != 0) q.push(make_pair(x,y));
        }
        
        spread();
        doAir();
    }
    int sum = 0;
    REP(i,r)
    REP(j,c) if(room[i][j] != -1) sum += room[i][j];
    cout << sum;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    solve();
}