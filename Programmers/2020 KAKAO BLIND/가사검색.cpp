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
    Trie* Node[MX];
    bool isFinished;
    bool hasChild;
    int nodeCount;
    Trie(){
        memset(Node,NULL,sizeof(Node));
        hasChild = isFinished = false;
        nodeCount = 1;
    }

    void insert(string s,int len, int index){
        
        if(index == len){
            isFinished = true;
            return;
        }
        
        int next = s[index] - 'a';
        
        if(Node[next] == NULL){
            Node[next] = new Trie();
            hasChild = true;
        }
        else Node[next]->nodeCount++;
        
        Node[next]->insert(s,len,index+1);
    }

    int find(string s,int len, int index){
        if(index == len){
            if(isFinished) return 1;
            else return 0;
        }
        if(s[index] == '?'){
            int temp = 0;
           REP(i,27){
               if(Node[i] != NULL) temp += Node[i]->nodeCount;
               
           }
           return temp;
        }
      
        int next = s[index] - 'a';
        if(Node[next] == NULL) return 0;
        return Node[next]->find(s,len,index+1);
                
    }
};


vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    Trie* trie[10010];
    Trie* reverseTrie[10010];
    for(auto e : words){
        int len = e.size();

        if(trie[len] == NULL) trie[len] = new Trie();
        trie[len]->insert(e,e.size(),0);
        if(reverseTrie[len] == NULL) reverseTrie[len] = new Trie();
        reverse(e.begin(),e.end());
        reverseTrie[len]->insert(e,e.size(),0);
    }
    for(auto e : queries){
        int len = e.size();

        if(e[0] == '?'){
            reverse(e.begin(),e.end());
            if(reverseTrie[len] == NULL) answer.push_back(0);
            else answer.push_back(reverseTrie[len]->find(e,e.size(),0));
        }
        else{
            if(trie[len] == NULL) answer.push_back(0);
            else answer.push_back(trie[len]->find(e,e.size(),0));
        }
        
    }

    return answer;
}

int main(){
    vector<string> words = {"frodo", "front", "frost", "frozen", "frame", "kakao"};
    vector<string> queries = {"fro??", "????o", "fr???", "fro???", "pro?"};
    solution(words,queries);
    
}



