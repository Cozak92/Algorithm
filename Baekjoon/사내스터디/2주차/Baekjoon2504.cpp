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


bool isValidated(string s) {
    stack<char> stack;

    for (char c: s) {
        if (c == '(') {
            stack.push(c);
        }
        if (c == '[') {
            stack.push(c);
        }
        if (c == ')') {
            if (!stack.empty() && stack.top() == '(') {
                stack.pop();
            } else {
                return false;
            }
        }
        if (c == ']') {
            if (!stack.empty() && stack.top() == '[') {
                stack.pop();
            } else {
                return false;
            }
        }
    }
    return true;
}

int calString(string s) {
    stack<char> stack;
    int num, top = 1;
    long long result = 0;

    REP(i, s.size()) {
        if (s[i] == '(') {

            num *= 2;

            stack.push('(');

        } else if (s[i] == '[') {

            num *= 3;

            stack.push('[');

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

    return result;
}


void solve() {
    string aaaa;
    cin >> aaaa;

    if (isValidated(aaaa)) {
        cout << calString(aaaa);
    } else {
        cout << 0;
    }


}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}