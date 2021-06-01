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

struct Trie{
    Trie* Node[26]; //알파벳 숫자만큼 크기 생성
    bool finish; // 문자열이 끝났는지 확인
    bool nextChild; // 문자열의 자식이 있는지 확인

    // 생성자
    Trie(){
        fill(Node, Node + 26, nullptr);
        finish = nextChild = false;

    }
    //소멸자
    ~Trie(){
        for (int i = 0; i < 26; i++)
            if (Node[i])
                delete Node[i];
    }

    int tonum(char c) {        //문자를 숫자로 변환.
        return tolower(c) - 'a';    //대문자인 경우는 소문자로 변환.
    }

    void insert(const char* words) {
        if (*words == '\0'){ //입력받은 words가 '\0'일 경우, 즉 문자열 끝인 경우.
            finish = true;
            return;
        }       
 
        int next = tonum(*words);
 
        if (Node[next] == NULL) {
            Node[next] = new Trie();
            nextChild = true;
        }
        Node[next]->insert(words + 1); // 문자열의 주소 + 1
    }

    bool find(const char* words) {
        int next = tonum(*words);
 
        if (*words == '\0') 
            return true;
 
        if (Node[next] == NULL)
            return false;
 
        return Node[next]->find(words + 1);
    }

    vector<string> startWith(const char* search){
        curr = Root;
        vector<string> result;

        
    }

};

void solve(){
  
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}