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

int t,n;

struct Trie{ //1
  Trie* Node[MX];
  bool isFinished;
  bool hasChild;

  Trie(){
    fill(Node,Node+MX,nullptr);
    isFinished = hasChild = false;
  }

  void insert(string s,int len,int index){
    if(index >= len){
      isFinished = true;
      return;
    }
    int next = s[index] - '0';
    if(Node[next] == NULL){
      Node[next] = new Trie();
      hasChild = true;
    }

    Node[next]->insert(s,len,index + 1);

  }

  bool find(string s,int len,int index){
    if(index >= len){
      if(hasChild) return false;
      else return true;
    }
    int next = s[index] - '0';
    if(isFinished) return false;
    return Node[next]->find(s,len,index + 1);
  }
};

bool solve(){ //2 
  cin >> n;
  vector<string> arr;
  Trie* trie = new Trie();
  REP(i,n){
    string s; cin >> s;
    trie->insert(s,s.size(),0);
    arr.push_back(s);
  }

  for(auto t : arr){
    if(!trie->find(t,t.size(),0)){
      return false;
    }
  }
  return true;

}

int main(){ //3
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> t;
    while(t--) cout << (solve() ? "YES\n" : "NO\n");
}