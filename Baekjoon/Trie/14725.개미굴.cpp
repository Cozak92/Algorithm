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
const int MX = 1;


struct Trie{
    map<string,Trie*> child;

    Trie(){}
    ~Trie(){
        for(auto it = child.begin(); it != child.end(); it++){
            delete (*it).second;
        }
    }
    void insert(vector<string> s,int len,int index){
        if(index == len) return;

        if(!child.count(s[index])){
            child[s[index]] = new Trie();
        }
        child[s[index]]->insert(s,len,index + 1);
    }

    void find(int depth){
        for(auto it = child.begin(); it != child.end(); it++){
            REP(i,depth) cout << "--";
            cout << (*it).first << "\n";
            (*it).second->find(depth + 1);
        }
    }

};

void solve(){
    int n; cin >> n;
    Trie* root =new Trie();

    REP(i,n){
        int k; cin >> k;
        vector<string> v(k);
        REP(j,k){
            cin >> v[j];
        }
        root->insert(v,k,0);
    }

    root->find(0);

  
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}