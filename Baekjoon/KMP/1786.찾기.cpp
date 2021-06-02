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
const int MX = 10;

string a,b;

// vector<int> getPi(string s){
//     int m = s.size();
//     vector<int> pi(m,0);

//     int matched = 0,start = 1;
//     while(start + matched < m){
//         if(s[start + matched] == s[matched]){
//             matched++;
//             pi[start + matched - 1] = matched;
//         }
//         else{
//             if(matched == 0){
//                 start++;
//             }
//             else{
//                 start += matched - pi[matched - 1]; // 시작위치 재설정
//                 matched = pi[matched - 1];
//             }
//         }
//     }
//     return pi;
// }

// vector<int> kmp(string src, string search){
//     int n = src.size(), m = search.size();
//     vector<int> ret;
//     vector<int> pi = getPi(search);

//     int start = 0, matched = 0;
//     while(start <= n - m ){
//         if (matched < m && src[start + matched] == search[matched]){
//             ++matched;
//             // 문자열이 모두 일치하는 경우
//             if (matched == m) ret.push_back(start);
//         }
//          else{
//             // 일치하는 부분이 없는 경우, 다음 위치의 문자 부터 탐색
//             if(matched == 0)
//                 ++start;
            
//             // 문자열이 불일치 하므로 접두사, 접미사 의 길이 만큼 건너 뜀!
//             else{
//                 // 현재 불일치가 발생한 위치는 begin + matched
//                 // 여기서 접두, 접미사의 길이인 pi[matched - 1] 을 빼주면 다음 탐색 시작 위치
//                 start += matched - pi[matched - 1];
//                 matched = pi[matched - 1];
//             }
//         }
//     }

// }

vector<int> getPi(string search){
    int m = search.size();
    int matched = 0;
    vector<int> pi(m,0);


    for(int start = 1; start < m; start++){
        while(matched > 0 && search[start] != search[matched]){
            matched = pi[matched - 1];
        }
        if (search[start] == search[matched]) {

				pi[start] = ++matched;
			}
		}

		return pi;

}

vector<int> kmp(string src, string search){
    int n = src.size(), m = search.size();
    vector<int> pi = getPi(search);
    // for(auto e : pi) cout << e << "\n";
    int matched = 0;
    vector<int> ret;

    for(int i = 0; i < n; i++){
        while(matched > 0 && src[i] != search[matched]){
            matched = pi[matched - 1];
        }

        if(src[i] == search[matched]){
            if(matched == n -1){
                ret.push_back(i - m  +1);
                matched = pi[matched];
            }
            else matched++;
        }
    }

    return ret;
}

void solve(){
  getline(cin, a);
  getline(cin, b);

  vector<int> ans = kmp(a,b);
    cout << ans.size() << "\n";
  for(auto e : ans) cout << e << " ";
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}