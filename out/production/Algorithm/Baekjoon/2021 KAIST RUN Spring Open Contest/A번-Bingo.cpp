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

int n,k;
int q[1000];

   
    
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    

    cin >> n >> k;
    int f = n - 2;
    REP(p,n){
        if(p == 0){
            q[p] = p;
        }
        else if(p == n - 1){
            q[p] = p;
        }
        else{
            q[p] = f;
            f--;
        }
    }

    if(n == 2){
        if(k > 1){
            cout << "NO";
            exit(0);
        }
        
    }
   
    if(k <= n*n -n){
        cout << "YES" << "\n";
        int cnt = 0;

        REP(i,n){
            REP(j,n){
                if(j == q[i]){
                    cout << ".";
                    continue;
                }
                if( cnt < k ){
                    cout << "#";
                    cnt++;
                }
                else cout << ".";

            }
            cout << "\n";
        }
        }
    else cout << "NO";


}