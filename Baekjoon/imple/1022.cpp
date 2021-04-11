#include<cstdio>
#include<algorithm>
using namespace std;
 
int f(int i, int j) {
    int n = max(abs(i), abs(j));
    int val = (2 * n + 1);
    val *= val;
 
    int diff = 2 * n;


    // 현재 꼭지점이 네 곳중에 어디에 위치해있는지 체크
    if (i == n)return val - (n - j); // 아랫줄 체크
    // diff = 이동칸수, j가 양수라면 n 보다 못감, j가 음수라면 n보다 더 감
    // 만약 i,j가 양수라면 그냥 val - (diff -i,j) 하면 원래 가는만큼 가겠지

    //현재 꼭지 점에 없다면 꼭지점 끼리의 차이만큼 빼고 다시 체크
    val -= diff;
    if (j == -n)return val - (n - i); // 왼쪽줄 체크
    val -= diff;
    if (i == -n)return val - (j + n); // 위쪽줄 체크
    val -= diff;
    // 없다면 오른쪽줄
    return val - (i + n);
}
 
int g(int val) {
    return val ? g(val / 10) + 1 : 0;
}
 
int main() {
    int r1, c1, r2, c2;
    scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
 
    int k=0;
    for (int i = r1; i <= r2; ++i)for (int j = c1; j <= c2; ++j)k = max(k, g(f(i, j)));
 
    for (int i = r1; i <= r2; ++i) {
        for (int j = c1; j <= c2; ++j)printf("%*d ", k, f(i, j));
        putchar('\n');
    }
 
}
