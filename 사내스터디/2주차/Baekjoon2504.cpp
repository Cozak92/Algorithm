//
// Created by cozak on 2022-03-02.
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


int calString(string s) {
    stack<char> stack;
    long long result = 0;
    bool isPossible = true;
    int num = 1;

    REP(i, s.size()) {
        if (s[i] == '(') {

            num *= 2;

            stack.push(s[i]);

        } else if (s[i] == '[') {

            num *= 3;

            stack.push(s[i]);

        } else if (s[i] == ')' && (stack.empty() || stack.top() != '(')) {

            isPossible = false;

            break;

        } else if (s[i] == ']' && (stack.empty() || stack.top() != '[')) {

            isPossible = false;

            break;

        } else if (s[i] == ')') {

            if (s[i - 1] == '(')
                result += num;

            stack.pop();

            num /= 2;

        } else if (s[i] == ']') {

            if (s[i - 1] == '[')
                result += num;

            stack.pop();

            num /= 3;
        }

    }

    if (!isPossible || !stack.empty())
        return 0;
    else
        return result;

}


void solve() {
    string aaaa;
    cin >> aaaa;

    cout << calString(aaaa);

}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}