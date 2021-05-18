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

int y;
int h;
int dp[20];
double a = 1.05;
double b = 1.2;
double c = 1.35;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> h >> y;
    
    // 그리디 실패 ㅜ
    // REP(i,(y / 5)) h += (h * c);
    // y %= 5;
    // REP(i,(y / 3)) h += (h * b);
    // y %= 3;
    // REP(i,y) h += (h * a);
    dp[0] = h;
    FOR(i,1,y+1){
        dp[i] = (int)dp[i-1] * a;
        if(i >= 3) dp[i] = max((int)(dp[i-3] * b), dp[i]);
        if(i >= 5) dp[i] = max((int)(dp[i-5] * c), dp[i]);
    }

    cout << dp[y];

}