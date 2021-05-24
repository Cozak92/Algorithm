#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << endl;
using ll = long long;
using pii = pair<int,int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;    
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 200100;

int n;
int arr1[MX];
int arr2[MX];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    REP(i,n) cin >> arr1[i];
    REP(j,n) cin >> arr2[j];

    int s = 0;
    int e = n-1;

    while(s <= e){
        int q =arr1[s] - arr2[e];
        
    }


}