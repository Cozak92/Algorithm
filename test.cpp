#include <iostream>

#include <cstring> //memset

using namespace std;

 

const int MAX = 100;

 

int N;

int operand[MAX]; //피연산자 집합

long long cache[20 + 1][MAX]; //연산 결과인 0~20, idx

 

long long numOfWays(int leftNum, int idx) //왼쪽에서부터 연산을 시작하므로 leftNum, idx는 여태까지 연산을 진행한 인덱스

{

        //기저 사례

        if (leftNum < 0 || leftNum>20)

               return 0;

        if (idx == N - 2) //조건에 맞는가

               return (leftNum == operand[N - 1]);

 

        long long &result = cache[leftNum][idx];

        if (result != -1)

               return result;

 

        result = 0;

        //더하거나 빼는 경우

        return result += (numOfWays(leftNum + operand[idx + 1], idx + 1) + numOfWays(leftNum - operand[idx + 1], idx + 1));

}

 

int main(void)

{

        cin >> N;

 

        for (int i = 0; i < N; i++)

               cin >> operand[i];

       

        memset(cache, -1, sizeof(cache));

        cout << numOfWays(operand[0], 0) << endl;

        return 0;

}
