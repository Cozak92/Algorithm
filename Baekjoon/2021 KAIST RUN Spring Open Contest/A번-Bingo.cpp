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

int n,k;
int board[1000][1000];
bool isVisited[1000][1000];
int isRowFilled[1000];
int isColumnFilled[1000];   
int isDiagonalFilled[1000];
int loop = 0;


void dfs(int x,int y,int cnt){
    // loop++;
    // if(loop == 1000) exit(0);
    // int x = cnt / n;
    // int y = cnt % n;
    cout << x << " " << y << endl;
    
    // if(isRowFilled[y] >= n) return;
    // if(isColumnFilled[x] >= n) return; 
    // if(isDiagonalFilled[(n - 1 + x - y)] >= n) return;
  
    if( cnt == k){
        cout << "YES" << "\n";
        REP(i,n){
            REP(j,n){
                if(board[i][j] == 0) cout << ".";
                else cout << "#";
            }
            cout << "\n";
        }
        exit(0);
    }

    REP(i,8){

        int nx = x + dx8[i];
        int ny = y + dy8[i];

        if( 0 <= nx && nx < n && 0 <= ny && ny < n && isVisited[nx][ny] != true){


            if(isRowFilled[ny] >= n -1) continue;
            if(isColumnFilled[nx] >= n -1) continue; 
            if(isDiagonalFilled[(n - 1 + nx - ny)] >= n - 1) continue;
            isRowFilled[ny]++;
            isColumnFilled[nx] ++; ;
            isDiagonalFilled[(n - 1 + ny - nx)] ++;
            isVisited[nx][ny] = true;
            board[nx][ny] = 1;
            dfs(nx,ny,cnt + 1);
            isVisited[nx][ny] = false;
            board[nx][ny] = 0;
            isRowFilled[ny]--;
            isColumnFilled[nx] --; 
            isDiagonalFilled[(n - 1 + ny - nx)] --;

        }
        
        
    }

}
   
    
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;

    if(n == 2){
        if(k != 1){
            cout << "NO";
            exit(0);
        }
    }
    if(k <= n*n -n){
        cout << "YES" << "\n";
        int index = n -1;
        int cnt = 0;
        REP(i,n){
            REP(j,n){
                if(j == index){
                    cout << ".";
                    index--;
                    continue;
                }
                if( cnt < k ){
                    cout << "#";
                    cnt++;
                }
                else cout << ".";

            }
            cout << "\n";
        }
    }
    else cout << "NO";
    // board[0][0] = 1;
    // isRowFilled[0]++;
    // isColumnFilled[0] ++; ;
    // isDiagonalFilled[(n - 1 + 0 - 0)] ++;
    // isVisited[0][0] = true;
    // dfs(0,0,1);
    // cout << "NO";


}