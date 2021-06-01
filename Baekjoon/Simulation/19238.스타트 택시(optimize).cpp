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


int board[MX][MX];
bool isCompleted[500];
bool isVisited[MX][MX];
int customerIndex[MX][MX];
int customers[500][4];
int reqFuel[500];
int n,m,fuel;
pii taxi;

struct info{
    int x,y,val,idx;
};
struct cmp{
    bool operator()(info &a, info &b){
        if(a.val==b.val){
            if(a.y==b.y)
                return a.x> b.x;
            return a.y > b.y;
        }
        return a.val > b.val;
    }
};

// 손님의 시작부터 - > 목적지까지의 연료
void findReqFuel(int a,int b, int xx, int yy,int index){
    queue<pair<int,pii>> q;
    memset(isVisited,false,sizeof(isVisited));
    q.push(make_pair(0,make_pair(a,b)));
    isVisited[a][b] = true;

    while(!q.empty()){
        int x = q.front().second.first;
        int y = q.front().second.second;
        int dist = q.front().first;
        q.pop();
        if( x == xx && y == yy){
            reqFuel[index] = min(dist,reqFuel[index]);

        }

        REP(i,4){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(0 < nx && nx <= n && 0 < ny && ny <= n && board[nx][ny] != 1){
                if(!isVisited[nx][ny]){
                     q.push(make_pair(dist + 1, make_pair(nx,ny)));
                     isVisited[nx][ny] = true;
                }
            }
        }
    }

}
// 현재 택시 시작 -> 손님 시작
int findMinDist(int a,int b){
    memset(isVisited,false,sizeof(isVisited));
    queue<info> q;
    priority_queue<info,vector<info>,cmp> pq;
    int arrivedAt = -1;
    info temp;
    temp.x = a;
    temp.y = b;
    temp.val = 0;
    isVisited[a][b] = true;
    q.push(temp);

    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        int dst = q.front().val;
        q.pop();
        if(customerIndex[x][y] && !isCompleted[customerIndex[x][y]]){
            temp.x = x;
            temp.y = y;
            temp.val = dst;
            temp.idx = customerIndex[x][y];
            pq.push(temp);
        }
        REP(i,4){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 < nx && nx <= n && 0 < ny && ny <= n && board[nx][ny] != 1){
                if(!isVisited[nx][ny]){
                    isVisited[nx][ny] = true;
                    temp.x = nx;
                    temp.y = ny;
                    temp.val = dst+1;
                    q.push(temp);

                }
                
            }
        }


    }

    if(!pq.empty()){
        arrivedAt = pq.top().idx;

        fuel -= pq.top().val;
        taxi.first = customers[arrivedAt][2];
        taxi.second = customers[arrivedAt][3];
        pq.pop();
    }
    return arrivedAt;
    

}

void solve(){
    cin >> n >> m >> fuel;

    memset(reqFuel,INF,sizeof(reqFuel));

    FOR(i,1,n+1)
    FOR(j,1,n+1){
         cin >> board[i][j];

    }
    int r,c; cin >> r >> c;
    taxi = {r,c};

    FOR(i,1,m+1){
        cin >> customers[i][0] >> customers[i][1] >> customers[i][2] >> customers[i][3];
        findReqFuel(customers[i][0], customers[i][1], customers[i][2], customers[i][3],i);
        customerIndex[customers[i][0]][customers[i][1]] = i;
    }

    REP(i,m){
        int curIndex = findMinDist(taxi.first,taxi.second);
        // debug(fuel);
        // debug(reqFuel[curIndex]);
        if(curIndex == -1){
            fuel = curIndex;
            break;
        }
        if(fuel >= reqFuel[curIndex]){
            fuel += reqFuel[curIndex];
            isCompleted[curIndex] = true;
        }
        else{
            fuel = -1;
            break;
        }

        // debug(fuel);
    }
    cout << fuel;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}