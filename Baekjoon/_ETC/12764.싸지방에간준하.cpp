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
constexpr double DINF = 1.79769e+308;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 100010;

struct Person{
    int start,end;

    bool operator < (const Person &a) const {
        return start < a.start;
    }
}people[MX];

int seat = 0;
int usedSeat[MX];
int n;


void solve(){
    priority_queue<pii> occupiedSeat; // 사용중인 자리
    set<int> unoccupiedSeat; // 빈 자리
    cin >> n;
    REP(i,n) cin >> people[i].start >> people[i].end;
    sort(people,people+n);

    REP(i,n){
        while (!occupiedSeat.empty()){ 
            if(-occupiedSeat.top().first <= people[i].start){ // 가장 빨리 끝나는 시간이 끝남 / 사용중인 자리가 끝났다는 뜻
                unoccupiedSeat.insert(occupiedSeat.top().second); // 끝난 자리를 반환;
                occupiedSeat.pop();
            }
            else break;
            
        }
        // 남은 자리가 없음
        if(unoccupiedSeat.empty()){
            occupiedSeat.push(make_pair(-people[i].end, seat));
            usedSeat[seat++]++;
           
        }
        // 남은자리가 있음
        else{
            auto leftSeat = unoccupiedSeat.begin();
            occupiedSeat.push(make_pair(-people[i].end, *leftSeat));
            usedSeat[*leftSeat]++;
            unoccupiedSeat.erase(leftSeat);
        }
        
    }
    cout << seat << "\n";

    REP(i,seat){
        cout << usedSeat[i] << " ";
    }
  
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}