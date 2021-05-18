// python3

    // def longestStrChain(self, words):
    //     dp = {}
    //     for w in sorted(words, key=len):
    //         dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
    //     return max(dp.values())

using namespace std;

 static bool compare(const string &s1, const string &s2) {
        return s1.length() < s2.length();
    }

int longestStrChain(vector<string>& words) {
    sort(words.begin(), words.end(), compare);
    unordered_map<string, int> dp;
    int res = 0;
    for (string w : words) {
        for (int i = 0; i < w.length(); i++) {
            string pre = w.substr(0, i) + w.substr(i + 1);
            dp[w] = max(dp[w], dp.find(pre) == dp.end() ? 1 : dp[pre] + 1);
        }
        res = max(res, dp[w]);
    }
    return res;
}