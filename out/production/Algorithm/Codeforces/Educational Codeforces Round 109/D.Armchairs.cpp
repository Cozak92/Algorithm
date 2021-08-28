#include <bits/stdc++.h>

using namespace std;

int n;
int dp[5050][5050];
vector<int> seated,freeSeat;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    

    cin >> n;
    seated.push_back(0); freeSeat.push_back(0);
    for(int i =1; i <= n; i ++){
        int a; cin >> a;
        // 0,1 각 각 벡터에 넣어줌;
        if(!a){
            freeSeat.push_back(i);
        }else seated.push_back(i);
    }

    
    int x = (int)seated.size() - 1; int y = (int)freeSeat.size() - 1;
    // 최소값에 이상한거 안들어오게 초기화;
    for(int i=1; i<=x; i++) dp[i][0] = 1010101010;
    

    for(int i = 1; i <= x; i++){
        for(int j = 1; j <= y; j++){
            // i번째 앉은사람이 j-1번째 의자로 이동하는것 
            // VS
            // i-1번째 앉은사람이 j-1번 의자로 이동하는것 +i번째 앉은 사람이 j번 의자로 이동하는것
            dp[i][j] = min(dp[i][j-1],dp[i-1][j-1] + abs(seated[i] - freeSeat[j]));
        }
    }

    cout << dp[x][y] << "\n";

}