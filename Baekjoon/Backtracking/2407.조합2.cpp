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

string cache[150][150];

string bigNum(string s1, string s2){
    int sum = 0;
    string ret;

    while(!s1.empty() || !s2.empty() || sum){
        if(!s1.empty()){
            sum += s1.back() - '0';
            s1.pop_back();

        }
        if(!s2.empty()){
            sum += s2.back() - '0';
            s2.pop_back();
        }
        ret.push_back((sum % 10) + '0');
        sum /= 10;
    }
    reverse(ALL(ret));
    return ret;
}


string combinations(int n, int r){
    if(r == n || r == 0) return "1";
    string &result = cache[n][r];

    if(result != "") return result;

    result = bigNum(combinations(n - 1,r - 1), combinations(n - 1, r));  
    return result;
}

void input(){
    
}

int main(){
    int n,m;
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> m;
    string ans = combinations(n,m);
    cout << ans;
}