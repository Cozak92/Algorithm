#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
// constexpr int MOD = 1000000007;
constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 510;

int h,w;
int R[MX + MX];
int B[MX + MX];
char board[MX][MX];

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  
  fill(R,R+MX,0);
  fill(B,B+MX,0);
  cin >> h >> w;
  
  FOR(i,1,h+1){
    FOR(j,1,w+1) cin >> board[i][j];
  }
  // 보드에 대각선에 서로 다른 색깔이 있으면 아무리 다른곳을 칠해도 길을 만들 수 없음;
  FOR(i,1,h+1){
    FOR(j,1,w+1){
      if(board[i][j] == 'R') R[i + j]++;
      else if(board[i][j] == 'B') B[i + j]++;
  }

  }
  
  ll ans = 1;
  FOR(k,2,h+w+1){
    if(R[k] && B[k]) ans *= 0;
    else if(!R[k] && !B[k]) ans = ans * 2 % MOD;
  }

    cout << ans << "\n";
}