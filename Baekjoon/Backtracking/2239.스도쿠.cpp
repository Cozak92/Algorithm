#include <iostream>

using namespace std;
#include<string>
int board[100][100];
bool isRowFilled[10][10];
bool isColumnFilled[10][10];
bool isSquareFilled[10][10];


void dfs(int cnt){



    if( cnt == 81){
        for(int i = 0; i<9; i++){
            for(int j =0; j <9; j++){
                cout << board[i][j];
            }
            cout << "\n";
        }
        exit(0);
    }

    int x = cnt / 9;
    int y = cnt % 9;
    if (board[x][y] == 0){
        for(int i =1; i < 10; i++){
            if(isRowFilled[x][i] || isColumnFilled[y][i] || isSquareFilled[(x/3)*3 +(y/3)][i]){
                continue;
            }
            isRowFilled[x][i] = true;
            isColumnFilled[y][i] = true;
            isSquareFilled[(x/3)*3 +(y/3)][i] = true;
            board[x][y] = i;
            dfs(cnt + 1);
            board[x][y] = 0;
            isRowFilled[x][i] = false;
            isColumnFilled[y][i] = false;
            isSquareFilled[(x/3)*3 +(y/3)][i] = false;
            
        }

    }
    else dfs(cnt+1);
    
}

void input(){
    
    for(int i = 0; i<9; i++){
        string temp;
        cin >> temp;
        for(int j =0; j <9; j++){
            board[i][j] = temp[j] - '0';
            if(board[i][j]){
                isRowFilled[i][board[i][j]] = true;
                isColumnFilled[j][board[i][j]] = true;
                isSquareFilled[(i/3) * 3+(j/3)][board[i][j]] = true;

            }
        }
    }
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(0);
    input();
    dfs(0);
}