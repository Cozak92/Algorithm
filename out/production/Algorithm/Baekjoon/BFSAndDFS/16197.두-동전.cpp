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
const int MX = 1;

int ans = INF;
vector<pair<int,int>> coins;
int n,m;
char board[50][50];

bool isOut(int x, int y){

    if (x < 0 || y < 0 || x >= n || y >= m) return true;
    return false;

}


void dfs(int x, int y , int xx, int yy ,int cnt){
    // cout << x << y << " " <<xx << yy << endl;
    if(cnt > 10){
        return;
    }
    if(isOut(x,y) && isOut(xx,yy)){
        return;
    }
    else if(isOut(x,y) || isOut(xx,yy)){
        ans = min(ans,cnt);
        return;
    }

    REP(i,4){
        int nx = x + dx[i];
        int ny = y + dy[i];
        int nxx = xx + dx[i];
        int nyy = yy + dy[i];

        if(!isOut(nx,ny) && board[nx][ny] == '#'){
            nx = x;
            ny = y;
        }
        if(!isOut(nxx,nyy) && board[nxx][nyy] == '#'){

            nxx = xx;
            nyy = yy;
        }

        dfs(nx,ny,nxx,nyy,cnt + 1);


    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;
    int k =0;

    REP(i,n){
        REP(j,m){
            cin >> board[i][j];
            if(board[i][j] == 'o'){
                coins.push_back(make_pair(i,j));

            }
        }
    }


    dfs(coins[0].first, coins[0].second, coins[1].first, coins[1].second, 0);

    if(ans == INF){
        cout << -1;
    }
    else cout << ans;
}