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
const int MX = 30;

struct Trie{
    Trie* Node[26];
    int nodeCount;
    Trie(){
        memset(Node,NULL,sizeof(Node));
        nodeCount = 1;
    }

    void insert(const char *str){
        
        if(*str == 0){
            return;
        }
        
        int next = *str - 'a';
        
        if(Node[next] == NULL){
            Node[next] = new Trie();
        }
        else Node[next]->nodeCount++;
        
        Node[next]->insert(str + 1);
    }

    int find(const char *str){
    
        if(*str == '?'){
            int temp = 0;
            REP(i,26){
               if(Node[i] != NULL) temp += Node[i]->nodeCount;
           }
           return temp;
        }
      
        int next = *str - 'a';
        if(Node[next] == NULL) return 0;
        return Node[next]->find(str + 1);
    }
};


vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    Trie *trie[10010];
    Trie *reverseTrie[10010];
    for(auto e : words){
        int len = e.size();

        if(trie[len] == NULL) trie[len] = new Trie();
        trie[len]->insert(e.c_str());

        if(reverseTrie[len] == NULL) reverseTrie[len] = new Trie();
        reverse(e.begin(),e.end());
        reverseTrie[len]->insert(e.c_str());
    }
    for(auto e : queries){
        int len = e.size();

        if(e[0] == '?'){
            reverse(e.begin(),e.end());
            if(reverseTrie[len] == NULL) answer.push_back(0);
            else answer.push_back(reverseTrie[len]->find(e.c_str()));
        }
        else{
            if(trie[len] == NULL) answer.push_back(0);
            else answer.push_back(trie[len]->find(e.c_str()));
        }
        
    }
    // for(auto e : answer) cout << e << "\n";
    return answer;
}

int main(){
    vector<string> words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
    vector<string> queries = {"fro??", "????o", "fr???", "fro???", "pro?"};
    solution(words,queries);
    
}



