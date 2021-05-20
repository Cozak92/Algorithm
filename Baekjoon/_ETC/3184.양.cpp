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

int r,c,sheeps,wolves;
char field[500][500];

void bfs(){
    queue<pair<int,int>> q;
    bool isVisited[500][500];
   

    REP(i,r){
        REP(j,c){
            if(!isVisited[i][j] && field[i][j] != '#'){
                q.push(make_pair(i,j));
                isVisited[i][j] = true;
                int curSheeps = 0;
                int curWolves = 0;

                if(field[i][j] == 'o') curSheeps++;
                if(field[i][j] == 'v') curWolves++;

               
                while(q.size()){

                    int x = q.back().first;
                    int y = q.back().second;
                    q.pop();
                    isVisited[x][y] = true;

                    REP(k,4){
                        
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        cout << nx << " " << ny << endl;
                        if( 0 <= nx && nx < r && 0 <= ny && ny < c && field[nx][ny] != '#'){
                            if(!isVisited[nx][ny]){
                                
                                if(field[nx][ny] == 'o'){
                                    cout << "isSheep" << endl;
                                    curSheeps++;
                                } 
                                else if(field[nx][ny] == 'v'){
                                    cout << "isWolves" << endl;
                                    curWolves++;
                                }
                                isVisited[nx][ny] = true;
                                q.push(make_pair(nx,ny));
                            }
                        }
                    }
                }
                cout << "CHECK" << endl;
                cout << curSheeps << " " << curWolves << endl;
                if(curSheeps > curWolves){
                    wolves -= curWolves;
                }
                else if (curSheeps <= curWolves){
                    sheeps -= curSheeps;
                }
            }
        }
    }

    
    
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> r >> c;
    REP(i,r){
        REP(j,c){
            cin >> field[i][j];
            if(field[i][j] == 'o') sheeps++;
            if(field[i][j] == 'v') wolves++;
        }
    }

    bfs();
    cout << sheeps << " " << wolves;


}