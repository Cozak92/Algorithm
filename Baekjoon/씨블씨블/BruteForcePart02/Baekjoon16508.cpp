//
// Created by cozak on 2022-02-06.
//

#include <bits/stdc++.h>

using namespace std;
#define FOR(i, m, n) for(int i=(m);i<(n);i++)
#define REP(i, n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define debug(x) cerr << #x << " is " << x << "\n"
using ll = long long;
using pii = pair<int, int>;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 10;
string T, w;
int N, c;
int answer = INF;
int target[26], combination[26];
struct Book {
    int price;
    string word;
};
vector<Book> books;

void dfs(int step, int totalSum) {
    if (step == N) {
        REP(i, 26) if (target[i] > combination[i]) return;
        answer = min(answer, totalSum);
        return;
    }

    string curWord = books[step].word;
    REP(i, curWord.size()) combination[curWord[i] - 'A']++;
    dfs(step + 1, totalSum + books[step].price);
    REP(i, curWord.size()) combination[curWord[i] - 'A']--;
    dfs(step + 1, totalSum);
}

void solve() {

    cin >> T;
    REP(i, T.size()) target[T[i] - 'A']++;
    cin >> N;
    REP(i, N) {
        cin >> c >> w;
        books.push_back({c, w});
    }
    dfs(0, 0);
    answer = (answer != INF) ? answer : -1;
    cout << answer;

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}