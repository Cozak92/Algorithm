#include <bits/stdc++.h>
using namespace std;
#define FOR(i,m,n) for(int i=(m);i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
using ll = long long;
constexpr int INF = 0x3f3f3f3f;
constexpr long long LINF = 0x3f3f3f3f3f3f3f3fLL;
constexpr double EPS = 1e-8;
constexpr int MOD = 1000000007;
// constexpr int MOD = 998244353;
constexpr int dy[] = {1, 0, -1, 0}, dx[] = {0, -1, 0, 1};
constexpr int dy8[] = {1, 1, 0, -1, -1, -1, 0, 1}, dx8[] = {0, -1, -1, -1, 0, 1, 1, 1};
const int MX = 30;

unordered_map<string,vector<string>> tree;

struct node{
    string left,right;
};
unordered_map<string,node> tree2;
int n;

void preDFS(string curNode){

    cout << curNode;
    if(tree2[curNode].left != ".")  preDFS(tree2[curNode].left);
    if(tree2[curNode].right != ".") preDFS(tree2[curNode].right);


}
void midDFS(string curNode){
    if(tree2[curNode].left != ".")  midDFS(tree2[curNode].left);
    cout << curNode;
    if(tree2[curNode].right != ".")  midDFS(tree2[curNode].right);
}
void postDFS(string curNode){

    if(tree2[curNode].left != ".")  postDFS(tree2[curNode].left);
    if(tree2[curNode].right != ".")  postDFS(tree2[curNode].right);
    cout << curNode;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    REP(i,n){
        string a, b, c;
        cin >> a >> b >> c;
        // tree[a].push_back(b);
        // tree[a].push_back(c);
        tree2[a].left = b;
        tree2[a].right = c;
    }

    preDFS("A");
    cout << endl;
    midDFS("A");
    cout << endl;
    postDFS("A");
    cout << endl;
}