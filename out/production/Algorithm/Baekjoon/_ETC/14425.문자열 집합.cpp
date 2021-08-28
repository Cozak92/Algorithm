#include <iostream> 
#include <unordered_map> 
#include <string> 
using namespace std; 
int N, M, cnt; 
string word; 
int main() { 
    ios::sync_with_stdio(false); 
    cin.tie(0); 
    cin >> N >> M;
    unordered_map<string, bool> m; 
    for (int i = 0; i < N; i++) { 
        cin >> word; m[word] = true; } 
    for (int i = 0; i < M; i++) { 
        cin >> word; 
        if (m[word]) cnt++; } 
    cout << cnt; }
