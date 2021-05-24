#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define what_is(x) cerr << #x << " is " << x << "\n"
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 200010 * 2;


struct braket{
    int val;
    int index;

    friend bool operator < (const braket &a, const braket &b){
        return a.val < b.val;
    }
}arr[MX];


int n;
int mark[MX];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n; n *= 2;
    FOR(i,1,n+1){
        cin >> arr[i].val;
        arr[i].index = i;
    }

    sort(arr + 1,arr+n+1);
    fill(mark,mark+MX,0);
    // 각각의 원소를 정렬하고 반씩 색을 칠해줌
    // 가장 큰 값의 괄호를 만들기 위해선 항상 가까운 쌍부터 먼 쌍으로 멀어져야함
    for(int i = 1; i < n/2 + 1; i++){
        
        mark[arr[i].index] = 1;
    }
    vector<int> stack;
    string ret(n + 1,' ');
    
    FOR(i,1,n+1){
        if(stack.empty() || mark[stack.back()] == mark[i]){
            stack.emplace_back(i);
        }
        else{
            ret[stack.back()] = '(';
            ret[i] = ')';
            stack.pop_back();
        }
    }
    cout << ret << "\n";
}