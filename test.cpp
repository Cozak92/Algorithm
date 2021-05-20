#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int n, k = 0;
	cin >> n >> k;
	int cnt = 0;
	string s;

	for (int i = 0; i <= n; i++) {
		for (int j = 0; j < 60; j++) {
			for (int l = 0; l < 60; l++) {
				if (i / 10 == 0) {
					s += "0";
				}
				s += to_string(i);
				if (j / 10 == 0) {
					s += "0";
				}
				s += to_string(j);
				if (l / 10 == 0) {
					s += "0";
				}
				s += to_string(l);
				if (s.find(to_string(k)) != -1) {
					cnt++;
				}
				s.clear();
			}
		}
	}
	std::cout << cnt;

	return 0;
}