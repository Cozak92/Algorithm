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
const int MX = 55;

struct info{
    int x,y,dist,key;
};

int n,m;
char board[MX][MX];
bool hasKey[MX][MX][1 << 8];
pii person;
bool exits[MX][MX];
int ans = INF;

void bfs(){
    // queue<pair<int ,pii>> q;
    queue<info> q;
    info temp;
    temp.x = person.first;
    temp.y = person.second;
    temp.dist = 0;
    temp.key = 0;

    hasKey[temp.x][temp.y][temp.key] = true;
    q.push(temp);

    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        int dist = q.front().dist;
        int key = q.front().key;
        q.pop();
        if(exits[x][y]){
            ans = min(ans,dist);
        }
        REP(i,4){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] != '#'){
                if(!hasKey[nx][ny][key]){
                    hasKey[nx][ny][key] = true;
                    if(isalpha(board[nx][ny])){
                        if(isupper(board[nx][ny])){ // 대문자
                            int thisKey = 1 << (board[nx][ny] - 'A'); 
                            if(thisKey & key){
                                temp.x = nx;
                                temp.y = ny;
                                temp.dist = dist + 1;
                                temp.key = key;
                                q.push(temp);
                            }
                            else continue; // 키가 없음
                        }
                        else{ // 소문자
                            int thisKey = 1 << (board[nx][ny] - 'a');
                            temp.x = nx;
                            temp.y = ny;
                            temp.dist = dist + 1;
                            temp.key = key | thisKey; // 키 넣기
                            q.push(temp);
                            
                        }
                    }
                    else{ //그냥 지나가는곳
                        temp.x = nx;
                        temp.y = ny;
                        temp.dist = dist + 1;
                        temp.key = key;
                        q.push(temp);
                    }
                }
            }

        }
    }
}

void solve(){
  cin >> n >> m;

  REP(i,n){
      REP(j,m){
           cin >> board[i][j];
           if(board[i][j] == '0'){
               person = make_pair(i,j);
           }
           if(board[i][j] == '1'){
               exits[i][j] = true;
           }
      }
  }

  bfs();
  cout << (ans == INF ? -1 : ans);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}