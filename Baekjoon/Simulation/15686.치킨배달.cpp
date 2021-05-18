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
int n,m;
int city[100][100];

vector<int> candidate;
int chikenNum,houseNum;
vector<pair<int,int>> house;
vector<pair<int,int>> chiken;

void findDist(int x, int y, int dist[]){
    int temp;
    REP(i,houseNum){
        temp = abs(x - house[i].first) + abs(y - house[i].second);
        dist[i] = min(dist[i],temp);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m;

    REP(i,n){
        REP(j,n){
            cin >> city[i][j];
            if(city[i][j] == 2) chiken.push_back(make_pair(i,j));
            if(city[i][j] == 1) house.push_back(make_pair(i,j));
        }
    }
    chikenNum = (int)chiken.size();
    houseNum = (int)house.size();
    // REP(i,m) candidate.push_back(1);
    // REP(i,chikenNum - m) candidate.push_back(0);

    vector<bool> v(chikenNum - m, false);
	v.insert(v.end(), m, true);
    
    int ans = INF;

    do{
        int dist[1000];
        memset(dist,INF,sizeof(dist));

        REP(i,chikenNum){
            if(v[i] == true){
                findDist(chiken[i].first, chiken[i].second, dist);
            }
        }
        
        int sum = 0;
        REP(j,houseNum){
            sum += dist[j];
        }
        ans = min(ans,sum);


    }while(next_permutation(ALL(v)));

    cout << ans;

}