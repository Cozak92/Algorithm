#include <iostream>
#include <vector>
#include <string>
using namespace std;

void test(int arr[][50]){
	arr[0][0] = 10;
}

int main() {
	int n, k = 0;
	int arr[50][50];
	arr[0][0] = 5;
	cout << arr[0][0] << endl;
	test(arr);
	cout << arr[0][0] << endl;
	return 0;
}