#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 1;

bool solve(){
    string s;
    cin >> s;
    int pCnt = 0;
    REP(i,s.size()){
        if(s[i] == 'P') pCnt++;
        else if(s[i] == 'A'){
            if(pCnt >= 2 && s[i+1] == 'P'){
                pCnt--;
                i++;
            }
            else return false;  
        }
        else return false;
    }
    if(pCnt == 1) return true;
    else return false;


}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cout << (solve() ? "PPAP\n" : "NP\n");
}