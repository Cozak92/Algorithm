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

int n;
int city[25][25];
int board[25][25];





// 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
// 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
// 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
// 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

void dfs(int x, int y, int val){
    
    if(board[x][y] != 0) return;
    board[x][y] = val;
    REP(i,4){
        int nx = x + dx[i];
        int ny = y + dy[i];
        if(0 <= x && x < n && 0<= y && y < n){
            dfs(nx,ny,val);
        }

    }

}

int makeBoard(int x, int y, int d1, int d2){
    // (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    // (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    // (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    // (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    // 5
    FOR(i,0,d1+1){
        board[x + i][y - i] = 5;
        board[x + d2 + i][y + d2 - i] = 5;
        // 0 , 1 ,0 = 1 , 0 , 1, 0

    }



    FOR(i,0,d2+1){
        board[x + i][y + i] = 5;
        board[x + d1 + i][y - d1 + i]  = 5;
    }
   
    // 1
    for(int i = x - 1; i >=0 ; --i){
        board[i][y] = 1;
    }
    //2
    for(int i = y + d2 + 1; i < n; ++i ){
        board[x + d2][i] = 2;
    }
    //3
    for(int i = y - d1 - 1 ; i >= 0; --i ){
        board[x + d1][i] = 3;
    }
    //4
    for(int i = x + d1 + d2 + 1; i < n; ++i){
        board[i][y - d1 + d2] = 4;
    }


    dfs(0,0,1);
    dfs(0,n-1,2);
    dfs(n-1,0,3);
    dfs(n-1,n-1,4);
    //     REP(i,n){
    //     REP(j,n){
    //         cout << board[i][j] << " ";
    //     }
    // cout << endl;
    // }
    int people[6] = {0};
    REP(i,n){
        REP(j,n){
            people[board[i][j]] += city[i][j];
        }
    }
    people[5] += people[0];

    int MAX = -INF;
    int MIN = INF;
    FOR(i,1,6){
        // cout << people[i] << endl;
        MAX = max(MAX,people[i]);
        MIN = min(MIN,people[i]);
 
    }
    
    
    memset(board,0,sizeof(board));

    return MAX - MIN;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    REP(i,n){
        REP(j,n) cin >> city[i][j];
    }
    int ans = INF;
    REP(x,n-2){
        REP(y,n-1){
            FOR(d1,1,n){
                FOR(d2,1,n){
                    //  1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N
                    
                    if(x + d1 + d2 > n - 1 || y - d1 < 0 || y + d2 > n - 1) continue;
                    ans = min(ans,makeBoard(x,y,d1,d2));
                }
            }
        }
    }

    cout << ans;
}